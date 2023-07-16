# 参考
- 学习b站视频 [https://www.bilibili.com/video/BV1zJ411w7SV?p=4](https://www.bilibili.com/video/BV1zJ411w7SV?p=4)
- location配置 [https://www.cnblogs.com/jpfss/p/10232980.html](https://www.cnblogs.com/jpfss/p/10232980.html)
- keepalived高可用 [https://www.jianshu.com/p/a6b5ab36292a](https://www.jianshu.com/p/a6b5ab36292a)

# 安装
```bash
# 查看OS版本
cat /etc/redhat-release 
CentOS Linux release 7.9.2009 (Core)

# 查看32位还是64位
getconf LONG_BIT
64

# nginx rewrite用到pcre
pcre-config --version
8.32

type pcre-config
pcre-config is hashed (/bin/pcre-config)

# 下载nginx源码http://nginx.org/en/download.html
wget http://nginx.org/download/nginx-1.22.0.tar.gz

# 解压
tar xzvf nginx-1.22.0.tar.gz

# 进入解压目录
cd nginx-1.22.0

# config
 ./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module

# 编译
make

# 安装
make install

# 查看nginx版本
cd /usr/local/nginx/sbin && ./nginx -v
nginx version: nginx/1.22.0

# 打开防火墙 
firewall-cmd --zone=public --add-port=80/tcp --permanent

# 重新加载
firewall-cmd --reload
```

# 基本命令
```shell
$ nginx -v     #查看版本
nginx version: nginx/1.18.0

$ nginx        #启动
$ ps -ef|grep nginx
root       1444      1  0 02:11 ?        00:00:00 nginx: master process nginx
nobody     1445   1444  0 02:11 ?        00:00:00 nginx: worker process
root       1447   1322  0 02:11 pts/0    00:00:00 grep --color=auto nginx

$ nginx -s stop #停止
$ ps -ef|grep nginx
root       1442   1322  0 02:10 pts/0    00:00:00 grep --color=auto nginx

$ nginx -t # 检查配置文件nginx.conf的正确性命令
nginx: the configuration file /usr/local/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /usr/local/nginx/conf/nginx.conf test is successful

$ nginx -s reload   # 重新载入配置文件
$ nginx -s reopen   # 重启 Nginx
$ nginx -s stop     # 停止 Nginx
```

# 配置文件
- /usr/local/nginx/conf/nginx.conf （`nginx -t`可查看配置文件位置）
- 配置文件分为三部分:
  - 全局块
  - events块
  - http块
    - 又分为http全局块
    - server块

## 第一部分 全局块
- 主要涉及nginx整体运行的一些配置

```
#user  nobody;
worker_processes  1; #支持并发处理数

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;
```

## 第二部分 events块
- 主要涉及用户与服务器网络连接配置

```
events {
    worker_connections  1024; #支持最大连接数
}
```

## 第三部分 http块
- 代理、缓存、日志等都在此配置，是nginx配置最频繁的地方

```
http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }

    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}
```

# 负载分配服务器策略

- 轮询（默认）
- 权重 weight(default 1)越大越高
- ip hash
- fair(根据服务器响应时间来分配、越快越先分配）

# 配置实例
## 反向代理实例

> 目标：浏览器输入www.test.com跳转到tomcat主界面

- 环境准备
    ```
    win10:   192.168.0.107
    nginx:   192.168.0.101:80
    Tomcat： 192.168.0.101:8080 (http redirect https)
    Tomcat2：192.168.0.101:8081
    Tomcat3：192.168.0.101:8082
    ```


- `/etc/hosts`文件修改
    ```
    192.168.0.101 www.test.com
    ```

- nginx.conf配置
    ```
    server {
        listen       80;
        #server_name  localhost;
        server_name  192.168.0.101;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
            proxy_pass   http://127.0.0.1:8081;
        }
    ```


## 反向代理实例2
```
server {
    listen       9001;
    #server_name  localhost;
    server_name  192.168.0.101;

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    location ~ /t1/ { # ~ 表示正则表达式
        root   html;
        index  index.html index.htm;
        proxy_pass   http://127.0.0.1:8081;
    }

    location ~ /t2/ {
        root   html;
        index  index.html index.htm;
        proxy_pass   http://127.0.0.1:8082;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
}
```

## 负载均衡实例
```
upstream mylbtest {
    server 192.168.0.101:8081;
    server 192.168.0.101:8082;
}

server {
    listen       80;
    #server_name  localhost;
    server_name  192.168.0.101;

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    location / {
        root   html;
        index  index.html index.htm;
        #proxy_pass   http://127.0.0.1:8081;
        proxy_pass   http://mylbtest;
    }

```

## 动静分离实例
```
location /image/ {
    root   www;
    index  index.html index.htm;
    autoindex on; #开启列目录
    # expires #有效期
}
```

## 高可用实例
- [keepalived使用参考](https://www.jianshu.com/p/a6b5ab36292a)
- 准备两台nginx
- 安装keepalived: `yum -y install keepalived`
- 配置虚拟ip:
    ```
    /etc/keepalived>cat keepalived.conf
    ! Configuration File for keepalived

    global_defs {
        router_id lb01
    }

    vrrp_script check {
        script "/usr/local/src/check_list.sh"
        interval  10
    }

    vrrp_instance VI_1 {
        state MASTER
        interface ens33
        virtual_router_id 50
        priority 150
        advert_int 1
        authentication {
            auth_type PASS
            auth_pass 1111
        }
        virtual_ipaddress {
            192.168.0.88
        }
        track_script  {
        check
        }
    }

    ```
- 检查脚本
    ```
    /etc/keepalived>cat /usr/local/src/check_list.sh
    #!/bin/sh

    nginxpid=$(ps -C nginx --no-header|wc -l)
    #1.判断Nginx是否存活,如果不存活则尝试启动Nginx
    if [ $nginxpid -eq 0 ];then
        /usr/local/nginx/sbin/nginx
        sleep 3
        #2.等待3秒后再次获取一次Nginx状态
        nginxpid=$(ps -C nginx --no-header|wc -l) 
        #3.再次进行判断, 如Nginx还不存活则停止Keepalived,让地址进行漂移,并退出脚本  
        if [ $nginxpid -eq 0 ];then
            killall keepalived
        fi
    fi
```
- 启动keepalived: `systemctl start keepalived.service`