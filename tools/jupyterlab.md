# jupyterlab安装配置

1. jupyterlab安装 `pip install jupyterlab`
1. jupyterlab配置:
    - 配置文件生成: `cd $HOME; jupyter lab --generate-config`,生成配置文件`$HOME/.jupyter/jupyter_lab_config.py`
    - 登录密码生成: `cd $HOME; jupyter lab password`,根据提示输入登录密码,生成加密后的文件`$HOME/.jupyter/jupyter_server_config.json`
    - 配置修改:
        ```
        c.ServerApp.ip='0.0.0.0'               # server listen on ip
        c.ServerApp.port=8080                  # server listen port
        c.ServerApp.allow_remote_access = True #允许远程访问
        c.ServerApp.password = '<$HOME/.jupyter/jupyter_server_config.json中的password>'  # 登录密码
        ```
1. 后台启动: `nohup jupyter lab &`
    - 也可在命令行指定参数启动: `nohup jupyter lab --port=8080 --ip='0.0.0.0' >> jupyter.log 2>&1 &`

# jupyterlab版本升级 

<p style="color: #303f9f;"><b>In:</b></p>

```python
import jupyterlab
print(jupyterlab.__version__)
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
!jupyter --version
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
!pip install --upgrade jupyterlab -i https://pypi.tuna.tsinghua.edu.cn/simple
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
!pip install nbclassic==0.2.8 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
name=''
name?
print
```
# 快捷键
## 编辑模式
```
- 自动补全: Tab
- 文档提示
    - Shift+Tab
    - 使用问号?
```
## 命令模式
```
命令模式 (按键 Esc 开启) 编辑模式(按键 Enter 切换)

Shift-Enter : 运行本单元，选中下个单元
Ctrl-Enter : 运行本单元
Alt-Enter : 运行本单元，在其下插入新单元
Y : 单元转入代码状态(命令模式下)
M :单元转入markdown状态(命令模式下)
R : 单元转入raw状态
1 : 设定 1 级标题
2 : 设定 2 级标题
3 : 设定 3 级标题
4 : 设定 4 级标题
5 : 设定 5 级标题
6 : 设定 6 级标题
Up : 选中上方单元
K : 选中上方单元
Down : 选中下方单元
J : 选中下方单元
Shift-K : 扩大选中上方单元
Shift-J : 扩大选中下方单元
A : 在上方插入新单元
B : 在下方插入新单元
X : 剪切选中的单元
C : 复制选中的单元
V : 粘贴到下方单元
Z : 恢复删除的最后一个单元
D,D : 删除选中的单元
Shift-M : 合并选中的单元
Ctrl-S : 文件存盘
S : 文件存盘
L : 转换行号
O : 转换输出
Shift-O : 转换输出滚动
Esc : 关闭页面
Q : 关闭页面
H : 显示快捷键帮助
Shift : 忽略
Shift-Space : 向上滚动
Space : 向下滚动
```

## 魔术符号

- % 行魔术 (写在一行)
- %% 格子魔术 (写在这个格子Cell里)
- %lsmagic 列举所有魔术符号

<p style="color: #303f9f;"><b>In:</b></p>

```python
%%time 
# 记录模块耗时
print('jupyter')
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
%lsmagic
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
%%html

<iframe src="https://www.bilibili.com/video/BV1614y1b7Bm/?spm_id_from=333.337.search-card.all.click" scrolling="no" width=100% height="800px" />
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
%%markdown

```
%%markdown
cell使用markdown
```
```
# 插件

## jupyterlab-drawio

<p style="color: #303f9f;"><b>In:</b></p>

```python
# !pip install jupyterlab-drawio
!pip install ipydrawio -i https://pypi.tuna.tsinghua.edu.cn/simple
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
from IPython.display import display,update_display
display({"application/x-drawio" : open("test.dio", "r")}, raw=True)
```
## jupyterlab集成PySpark

1. 安装PySpark: `pip install PySpark`
1. 获取spark关于py4j的文件信息: `ls $SPARK_HOME/python/lib/py4j-*-src.zip`
1. 在.bash_profile中配置环境变量:
    ```
    export SPARK_HOME=<your spark setup path>
    export PYSPARK_DRIVER_PYTHON=jupyter
    export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.3-src.zip:$PYTHONPATH
    ```
1. 重启jupyterlab
1. 通过`import pyspark`是否报错来检查是否集成成功

<p style="color: #303f9f;"><b>In:</b></p>

```python
pip install PySpark
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
import pyspark
pyspark.__version__
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
import os

df = spark.read.json(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.json")
df.show()
```
## pgywalker

<p style="color: #303f9f;"><b>In:</b></p>

```python
import pandas as pd
import pygwalker as pyg

json_data=[
    {'name': 'name1','age': 10},
    {'name': 'name2','age': 20},
    {'name': 'name3','age': 30},
    {'name': 'name4','age': 40},
]

df=pd.json_normalize(json_data)
# display(df)

gwalker=pyg.walk(df)
```
## jupyterlab集成plantuml
- https://github.com/jbn/IPlantUML/blob/master/README.rst
- https://stackoverflow.com/questions/20303335/ipython-notebook-plantuml-extension


```
pip install iplantuml

import iplantuml

cell magic:
%%plantuml --jar
```

<p style="color: #303f9f;"><b>In:</b></p>

```python
import iplantuml
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
# %%plantuml -h

# usage: ipykernel_launcher.py [-h] [-j] [-n NAME] [-p PLANTUML_PATH]

# optional arguments:
#   -h, --help            show this help message and exit
#   -j, --jar             render using plantuml.jar (default is plantweb)
#   -n NAME, --name NAME  persist as <name>.uml and <name>.svg after rendering
#   -p PLANTUML_PATH, --plantuml-path PLANTUML_PATH
#                         specify PlantUML jar path
#                         (default=/usr/local/bin/plantuml.jar)
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
%plantuml -h
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
%%plantuml -h

@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
@enduml
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
%%plantuml 

' @startmindmap routemap
@startwbs routemap

* 大数据

** python3
*** 开发环境
**** visual studio code
**** jupyterlab(notebook)
***** 集成PySpark
***** 集成plantuml
***** 集成SQL(mysql)

*** python基础
*** 框架/包
**** Flask(web)
**** jieba(中文分词库)
**** requests+json(http)
**** apscheduler(调度)

** 常用组件
*** PySpark(Spark)
**** SparkSQL
**** Spark Structured Streaming
**** GraphFrames

*** Hadoop
**** HDFS
**** YARN
**** MapReduce

*** Hive
**** metadata
*** Kafka

** 应用
*** 数据分析
**** numpy
**** pandas

*** 数据可视化
**** pyecharts\n(echarts)
**** PygWalker\n(Graphic Walker-Tableau)
**** matplotlib

*** 数据治理
**** sqllineage(分析SQL血缘)
**** apache atlas
**** 图数据库
***** HugeGraph
****** HugeGraph Server
****** HugeGraph Loader
****** HugeGraph Hubble(UI)
***** JanusGraph
***** Neo4j
***** Gremlin Query Language
**** 搜索引擎
***** solr

** 云平台
*** Azure Data Factory
*** Azure Databricks
**** Spark
**** delta lake(Lake House)
*** Azure Event Hub

' @endmindmap
@endwbs
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #fddfdd; padding-top: 5px">
UsageError: Cell magic `%%plantuml` not found.&#xA;</pre>
## jupyterlab统计cell耗时
- https://github.com/deshaw/jupyterlab-execute-time

<p style="color: #303f9f;"><b>In:</b></p>

```python
pip install jupyterlab_execute_time
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
import time
time.sleep(5)
```
## jupyterlab-lsp
- https://github.com/jupyter-lsp/jupyterlab-lsp

### 安装jupterlab-lsp

<p style="color: #303f9f;"><b>In:</b></p>

```python
pip install jupyterlab-lsp  -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 安装语言服务器

<p style="color: #303f9f;"><b>In:</b></p>

```python
pip install python-lsp-server[all]  -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### python提示加速

<p style="color: #303f9f;"><b>In:</b></p>

```python
%config Completer.use_jedi = False
```
- 永久加速配置修改:
`jupyter_lab_config.py`添加配置`c.Completer.use_jedi=False`


<p style="color: #303f9f;"><b>In:</b></p>

```python
from pandas import DataFrame
import pandas as pd

# pd.read_csv
import os
pd.read_sql_query
```