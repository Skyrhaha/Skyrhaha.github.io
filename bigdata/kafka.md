## Kafka安装
1. 下载安装
  ```bash
  cd /export/server
  wget http://archive.apache.org/dist/kafka/2.6.0/kafka_2.12-2.6.0.tgz
  tar xzvf kafka_2.12-2.6.0.tgz
  ln -s kafka_2.12-2.6.0 kafka
  ```

2. 配置修改
  ```xml
  #编辑 kafka/config/server.properties
  #broker.id=0 
  #port=9092 #端口号 
  #host.name=localhost #单机可直接用localhost
  #log.dirs= #日志存放路径可修改可不修改
  zookeeper.connect=localhost:2181 #zookeeper地址和端口，单机配置部署，localhost:2181 
  ```

3. 启动
  ```bash
  ./kafka-server-start.sh -daemon  ../config/server.properties

  # 停止(如果无法停止,使用kill -9强制停止)
  ./kafka-server-stop.sh
  ```

## 使用
查看topic情况
--describe