## 概述
- 参考
  - [官网文档](https://docs.janusgraph.org/getting-started/installation/)
  - [中文文档](http://www.janusgraph.cn/getting-started/installation.html)
  - [下载](https://github.com/JanusGraph/janusgraph/releases)
- janusgraph
- Gremlin语言
- janusGraph访问
  - gremlin console

## 安装
```bash
# 下载janusgraph-0.6.2.zip

unzip janusgraph-0.6.2.zip

cd janusgraph-0.6.2/

# 启动
bin/janusgraph-server.sh start
   # 报错查看hs_err_pid25845.log文件显示内存不足
   # 修改conf/jvm-8.options配置文件
   # -Xms1024m
   # -Xmx1024m
   # 重新启动成功

#查看端口监听
netstat -an|grep 8182 
```

## Console连接
```bash
#使用控制台连接(注意内存大小)
bin/gremlin.sh
         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/home/dev/setup/janusgraph-0.6.2/lib/slf4j-log4j12-1.7.30.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/home/dev/setup/janusgraph-0.6.2/lib/logback-classic-1.1.3.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
plugin activated: tinkerpop.server
plugin activated: tinkerpop.tinkergraph
17:33:35 WARN  org.apache.hadoop.util.NativeCodeLoader  - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
plugin activated: tinkerpop.hadoop
plugin activated: tinkerpop.spark
plugin activated: tinkerpop.utilities
plugin activated: janusgraph.imports
gremlin> 
gremlin> 
gremlin> 

// 连接远程GremlinServer
gremlin> :remote connect tinkerpop.server conf/remote.yaml
==>Configured localhost/127.0.0.1:8182

// 切换为远程服务(再一次切换为本地服务)
gremlin> :remote console

// 使用inmemory且无index配置
gremlin> graph = JanusGraphFactory.open('conf/janusgraph-inmemory.properties')
==>standardjanusgraph[inmemory:[127.0.0.1]]

// 加载GraphOfTheGods
gremlin> GraphOfTheGodsFactory.loadWithoutMixedIndex(graph, true)
==>null

// 遍历
gremlin> g = graph.traversal()
==>graphtraversalsource[standardjanusgraph[inmemory:[127.0.0.1]], standard]
gremlin> 

// 查询所有边
gremlin> g.E().valueMap(true)
==>{id=938-9i8-6c5-3aw, label=father}
==>{id=9hg-9i8-74l-co0, label=mother}
==>{id=9vo-9i8-7x1-36w, label=battled, time=1, place=POINT (23.700001 38.099998)}
==>{id=ao4-9i8-7x1-388, label=battled, place=POINT (22 39), time=12}
...

// 查询所有顶点
gremlin> g.V().valueMap(true)
==>{id=4128, label=titan, name=[saturn], age=[10000]}
==>{id=8224, label=location, name=[sea]}
==>{id=12320, label=demigod, name=[hercules], age=[30]}
==>{id=16416, label=human, name=[alcmene], age=[45]}
==>{id=20512, label=god, name=[pluto], age=[4000]}
==>{id=24608, label=monster, name=[hydra]}
==>{id=4136, label=monster, name=[nemean]}
==>{id=4184, label=monster, name=[cerberus]}
==>{id=4280, label=god, name=[jupiter], age=[5000]}
==>{id=8376, label=god, name=[neptune], age=[4500]}
==>{id=4336, label=location, name=[sky]}
==>{id=8432, label=location, name=[tartarus]}

// 查询拥有属性name='sea'的顶点
gremlin> g.V().has('name','sea').valueMap(true)
==>{id=8224, label=location, name=[sea]}
``` 
!> **:remote console** <br/>
此模式下不能使用变量(添加session可以使用变量) <br/>
:remote connect tinkerpop.server conf/remote.yaml session

## 显示schema信息
> 编写groovy脚本`display_schema_info.groovy`
```groovy
/**
 * gremlin> :load data/janusgraph-schema-grateful-dead.groovy
 * ==>true
 * ==>true
 * gremlin> t = JanusGraphFactory.open('conf/janusgraph-cql.properties')
 * ==>standardjanusgraph[cassandrathrift:[127.0.0.1]]
 * gremlin> displaySchemaInfo(t)
 * ==>null
 * gremlin> t.close()
 * ==>null
 * gremlin>
 */

def displaySchemaInfo(janusGraph) {
    m = janusGraph.openManagement()
    m.printSchema()
}
```

> 运行groovy脚本
```
// 加载脚本
gremlin> :load data/demo/display_schema_info.groovy
==>null
==>null

// 执行脚本
gremlin> displaySchemaInfo(graph)
==>------------------------------------------------------------------------------------------------
Vertex Label Name              | Partitioned | Static                                             |
---------------------------------------------------------------------------------------------------
titan                          | false       | false                                              |
location                       | false       | false                                              |
god                            | false       | false                                              |
demigod                        | false       | false                                              |
human                          | false       | false                                              |
monster                        | false       | false                                              |
---------------------------------------------------------------------------------------------------
Edge Label Name                | Directed    | Unidirected | Multiplicity                         |
---------------------------------------------------------------------------------------------------
father                         | true        | false       | MANY2ONE                             |
mother                         | true        | false       | MANY2ONE                             |
battled                        | true        | false       | MULTI                                |
lives                          | true        | false       | MULTI                                |
pet                            | true        | false       | MULTI                                |
brother                        | true        | false       | MULTI                                |
---------------------------------------------------------------------------------------------------
Property Key Name              | Cardinality | Data Type                                          |
---------------------------------------------------------------------------------------------------
name                           | SINGLE      | class java.lang.String                             |
age                            | SINGLE      | class java.lang.Integer                            |
time                           | SINGLE      | class java.lang.Integer                            |
reason                         | SINGLE      | class java.lang.String                             |
place                          | SINGLE      | class org.janusgraph.core.attribute.Geoshape       |
---------------------------------------------------------------------------------------------------
Graph Index (Vertex)           | Type        | Unique    | Backing        | Key:           Status |
---------------------------------------------------------------------------------------------------
name                           | Composite   | true      | internalindex  | name:         ENABLED |
---------------------------------------------------------------------------------------------------
Graph Index (Edge)             | Type        | Unique    | Backing        | Key:           Status |
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
Relation Index (VCI)           | Type        | Direction | Sort Key       | Order    |     Status |
---------------------------------------------------------------------------------------------------
battlesByTime                  | battled     | BOTH      | time           | desc     |    ENABLED |
---------------------------------------------------------------------------------------------------
```

