### HBase安装
1. 下载安装
  ```bash
  # 进入安装目录
  cd /export/server

  # 下载完整包
  wget http://archive.apache.org/dist/hbase/2.4.9/hbase-2.4.9-bin.tar.gz

  # 解压
  tar xzvf hbase-2.4.9-bin.tar.gz

  # 创建链接
  ln -s hbase-2.4.9 hbase
  ```

2. 配置文件hbase/conf/hbase-site.xml修改
  ```xml
    <property>
      <name>hbase.rootdir</name>
      <value>file:///export/data/hbase/root</value>
    </property>
    <property>
      <name>hbase.tmp.dir</name>
      <value>/export/data/hbase/tmp</value>
    </property>
  ```
3. 防火墙端口开放
  ```bash
  firewall-cmd --permanent --zone=public --add-port=16010/tcp
  firewall-cmd --reload
  firewall-cmd --zone=public --list-ports
  ```
4. 启动
  ```bash
  # 启动
  bin/start-hbase.sh

  # 停止
  bin/stop-hbase.sh

  # 检查状态
  bin/hbase在交换命令行输入status
  ```

5. 访问
> `http://<ip地址>:16010/master-status`
>
  ```bash
  bin/hbase
  hbase:002:0> status
  1 active master, 0 backup masters, 1 servers, 0 dead, 2.0000 average load
  Took 0.7231 seconds                                                                                                                                                               
  hbase:003:0> 
  ```
!> HBase自带zookeeper