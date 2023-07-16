<!-- # atlas {docsify-ignore} -->
## 代码编译(外部hbase+solr方式)
避免踩坑

!> 
atlas只有源码，安装包需要自行编译,请在github下载对应源码;官网源码可能有问题 <br/>
atlas编译对jdk版本有要求，至少jdk1.8 151之上 <br/>
代码子项目dashboardv3/package.json中node-sass版本一定要根据jdk的版本设置(巨坑) <br/>
如果使用内嵌HBase+Solr编译,请提前下载好HBase,Solr <br/>
最好使用外部Hbase+Solr编译

1. 安装文档参考https://atlas.apache.org/#/BuildInstallation
2. 从github下载atlas代码 atlas-branch-2.0.zip
3. 编译(windows 10)
  ```bash
  set MAVEN_OPTS=-Xms1g -Xmx1g
  set JAVA_HOME=C:\Program Files (x86)\Java\jdk1.8.0_181

  # 这里选择外部HBase+Solr安装
  # mvn clean -DskipTests package -Pdist,embedded-hbase-solr
  mvn clean -DskipTests package -Pdist
  ```

4. 编译问题1: UI子项目死活编译不过,提示python相关的错
   - pom.xml中注释dashboardv2子项目,使用dashboardv3即可
   - pom.xml中修改node.js版本,为本地安装的node.js版本号(我的是v16.5.0)
   - 设置node.js源为国内taobao源
    ```bash
    npm config set registry https://registry.npm.taobao.org --global
    npm config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/
    ```
    - 修改子项目dashboardv3/package.json中node-sass版本(我的是"node-sass": "^6.0.1")
      - 具体版本如何获得(参考https://blog.csdn.net/baobao_123456789/article/details/116047109)
      - node.js版本信息 https://nodejs.org/zh-cn/download/releases/
      - node-sass对应版本下载 https://github.com/sass/node-sass/releases/tag/v6.0.1

5. 编译问题2: HBase,Solr下载不下来(这是刚开始使用内嵌HBase+Solr遇到的问题)
   - 单独下载HBase,Solr
   - 将下载的安装包放置在 distro/hbase与distro/solr目录下
   - 修改pom.xml文件：注释掉其中 hbase与solr get maven goal步骤

6. 编译好之后启动报错:java.lang.NoClassDefFoundError: org/apache/htrace/core/HTraceConfiguration
   - 这是HBase缺少jar包导致
   - 复制lib/client-facing-thirdparty/htrace-core4-4.2.0-incubating.jar到hbase/lib下即可

7. 安装包获取
> distro下`apache-atlas-{project.version}-server.tar.gz`即为我们需要的安装包

## 环境部署

> [!NOTE|label:前置条件]
- [Hbase安装](hbase.md)
- [Solr安装](/database/solr.md)
- [Kafka安装](kafka.md)

### Atlas安装(外部hbase+solr方式)
1. 上传安装
  ```bash
  上传编译好的安装包apache-atlas-2.3.0-SNAPSHOT-server.tar.gz
  cd setup #非root安装
  tar xzvf apache-atlas-2.3.0-SNAPSHOT-server.tar.gz
  cd apache-atlas-2.3.0-SNAPSHOT
```

2. 配置-集成外部HBase
  ```
  # 编辑conf/atlas-application.properties:
  atlas.graph.storage.hostname=localhost:2181 # HBase自带的zookeeper

  # 编辑conf/atlas-env.sh:
  export HBASE_CONF_DIR=/export/server/hbase/conf
  ```

3. 配置-集成外部Solr & Solr初始化
  ```
  # 编辑conf/atlas-application.properties:
  atlas.graph.index.search.backend=solr 
  atlas.graph.index.search.solr.mode=cloud 
  atlas.graph.index.search.solr.zookeeper-url=localhost:2181

  # 创建solr core
  solr create  -c vertex_index -force
  solr create -c edge_index -force
  solr create -c fulltext_index -force
  ```

4. 配置-集成外部Kafka
  ```
  # 编辑conf/atlas-application.properties:
  atlas.notification.embedded=false
  atlas.kafka.data=${sys:atlas.home}/data/kafka
  atlas.kafka.zookeeper.connect=localhost:2181
  atlas.kafka.bootstrap.servers=localhost:9026
  ```

5. Atlas端口开放
  ```bash
  firewall-cmd --permanent --zone=public --add-port=21000/tcp
  firewall-cmd --reload
  firewall-cmd --zone=public --list-ports
  ```

6. 启动
  ```bash
  # 启动
  bin/atlas_start.py

  # 停止
  bin/atlas_stop.py
  ```

7. 访问
  `http://<ip>:21000/login.jsp` 默认用户名/密码: `admin/admin`

## REST API使用
### token设置
```python
# 用户名/密码以admin/admin为例
# token设置示例如下代码所示

host=os.environ['ATLAS_HOSTNAME']
port=21000
username='admin'
password='admin'
url=f"http://{host}:{port}/api/atlas/v2/types/typedefs"

token = str(base64.b64encode(bytes(f'{username}:{password}', encoding='utf8')), encoding='utf8')

response = requests.post(url=url, headers={ 'Authorization': f'Basic {token}'}, json=reqbody)

print(response.text)

# 注意: curl小技巧
# curl -u 'admin:123456' http://xxx
# 等同于
# curl -v -H 'Authorization: Basic YWRtaW46MTIzNDU2' http://xxx
```