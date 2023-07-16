## HugeGraph-Server
### 安装
```bash
# 下载源代码
wget https://github.com/apache/incubator-hugegraph/archive/refs/tags/v0.12.0.zip
unzip v0.12.0.zip
cd incubator-hugegraph-0.12.0
mvn clean package -DskipTests

cd hugegraph-0.12.0

# 后端存储配置修改
vi conf/graphs/hugegraph.properties
# 修改以下内容
backend=memory
serializer=text

# rest api配置修改
vi conf/rest-server.properties
# 修改以下内容
restserver.url=http://<ip address>:<port>

# 启动
bin/start-hugegraph.sh 

# 检查启动是否正常(返回200表示启动成功)
echo `curl -o /dev/null -s -w %{http_code} "http://<ip address>:<port>/graphs/hugegraph/graph/vertices"`

# 停止
bin/stop-hugegraph.sh
```

### 配置mysql后端存储
1. 配置修改
   ```bash
   cd hugegraph-0.12.0
   vi conf/graphs/hugegraph.properties
   # 修改以下内容
   backend=mysql
   serializer=mysql

   # mysql backend config
   jdbc.driver=com.mysql.jdbc.Driver
   jdbc.url=jdbc:mysql://<mysql host>:<mysql port>
   jdbc.username=root
   jdbc.password=<password>
   jdbc.reconnect_max_times=3
   jdbc.reconnect_interval=3
   jdbc.sslmode=false
   ```

2. 给数据库用户(如dev)添加`hugegraph`数据库访问权限
   ```sql
   GRANT ALL PRIVILEGES ON `hugegraph`.* TO 'dev'@'%';
   FLUSH PRIVILEGES;
   ```

3. 重新启动
   ```bash
   # 停止
   bin/stop-hugegraph.sh

   # 数据库初始化
   bin/init-store.sh

   # 启动
   bin/start-hugegraph.sh 

   # navicat连接mysql数据库并查看hugegraph数据已存在
   ```

## HugeGraph-Loader
### 安装
```bash
git clone https://github.com/apache/incubator-hugegraph-toolchain.git
cd incubator-hugegraph-toolchain
git tag -n
git checkout v0.12.0
git status

cd .. 
wget https://download.oracle.com/otn-pub/otn_software/jdbc/1815/ojdbc8.jar
mvn install:install-file -Dfile=./ojdbc8.jar -DgroupId=com.oracle -DartifactId=ojdbc8 -Dversion=12.2.0.1 -Dpackaging=jar

cd incubator-hugegraph-toolchain
mvn clean package -DskipTests

# hugegraph-loader-0.12.0/ 目录即为编译结果目录
```

### 使用示例
1. 查看示例数据
   ```bash
   # 查看示例数据
   ls -l example/file/
   total 28
   -rw-rw-r-- 1 dev dev  310 Oct  3 16:59 edge_created.json
   -rw-rw-r-- 1 dev dev  167 Oct  3 16:59 edge_knows.json
   -rw-rw-r-- 1 dev dev 1981 Oct  3 16:59 schema.groovy
   drwxrwxr-x 2 dev dev 4096 Oct  4 07:55 struct
   -rw-rw-r-- 1 dev dev 1330 Oct  3 16:59 struct.json
   -rw-rw-r-- 1 dev dev  125 Oct  3 16:59 vertex_person.csv
   -rw-rw-r-- 1 dev dev  101 Oct  3 16:59 vertex_software.txt
   ```

2. 导入
   ```bash
   # 示例数据导入
   sh bin/hugegraph-loader.sh -g hugegraph -f example/file/struct.json -s example/file/schema.groovy -h <host:localhost> -p <port:8080>
   >> HugeGraphLoader worked in NORMAL MODE
   vertices/edges loaded this time : 8/6
   --------------------------------------------------
   count metrics
      input read success            : 14                  
      input read failure            : 0                   
      vertex parse success          : 8                   
      vertex parse failure          : 0                   
      vertex insert success         : 8                   
      vertex insert failure         : 0                   
      edge parse success            : 6                   
      edge parse failure            : 0                   
      edge insert success           : 6                   
      edge insert failure           : 0                   
   --------------------------------------------------
   meter metrics
      total time                    : 0.445s              
      read time                     : 0.258s              
      load time                     : 0.187s              
      vertex load time              : 0.079s              
      vertex load rate(vertices/s)  : 101                 
      edge load time                : 0.126s              
      edge load rate(edges/s)       : 47                
   ```

## HugeGraph-Hubble
1. 源代码方式(编译target缺少ui部分,无页面)
   ```bash
   cd incubator-hugegraph-toolchain
   git tag -n
   git checkout v1.16.0
   git status

   mvn package -DskipTests

   # hugegraph-hubble-1.6.0/ 目录即为编译结果目录
   ```

   改用bin包安装
   ```bash
   wget https://github.com/hugegraph/hugegraph-hubble/releases/download/v1.6.0/hugegraph-hubble-1.6.0.tar.gz
   tar xzvf hugegraph-hubble-1.6.0.tar.gz
   ```

2. 修改配置
   ```bash
   cd hugegraph-hubble-1.6.0/

   # 修改host与port
   vi conf/hugegraph-hubble.properties
      server.host=<your host>
      server.port=<your port>
   ```

3. 启停
   ```bash
   # 启动
   bin/start-hubble.sh

   # 运行检查
   jps
   9939 HugeGraphHubble
   10231 Jps
   3146 HugeGraphServer

   # 停止
   bin/stop-hubble.sh
   ```

4. 访问
   `http://<host>:<port>/`

   - 创建图(首先在此配置HugeGraph Server信息才能使用)