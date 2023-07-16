# Spark环境搭建

## Spark安装(linux)
```bash
# 下载
wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz

# 解压至 /export/server/
mkdir /export/server
tar -zxvf spark-3.2.1-bin-hadoop3.2.tgz -C "/export/server"

# 创建软链接
ln -s /export/server/spark-3.2.1-bin-hadoop3.2/ /export/server/spark

# 运行bin/pyspark命令
cd /export/server/spark/; bin/pyspark => JAVA_HOME is not set

# jdk安装:
tar -zxvf /home/dev/jdk-8u161-linux-x64.tar.gz -C /export/server
ln -s jdk1.8.0_161/ jdk8
vi /etc/profile # 添加JAVA_HOME环境变量
export JAVA_HOME=/export/server/jdk8
export PATH=$PATH:$JAVA_HOME/bin

# 再次执行bin/pyspark => env: python3: No such file or directory
# Anaconda3安装:
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
sh Anaconda3-2022.05-Linux-x86_64.sh
# 依次输入 enter => yes => /export/server/anaconda3 => yes 安装完成
# 重新登录linux终端看见(base)开头表示安装成功
vi /etc/profile # 添加PYSPARK_PYTHON环境变量
export PYSPARK_PYTHON=/export/server/anaconda3/bin/python

# 再次执行/export/server/spark>bin/pyspark => pyspark启动成功，进入交互页面
```

## 示例运行
1. 通过`pyspark`启动交互式运行
   ```python
    >>> sc.parallelize([1,2,3,4,5]).map(lambda x: x+1).collect()
    [2, 3, 4, 5, 6]                                                                 
    >>> 
    ```
1. 检查4040端口
    ```bash
    netstat -anp|grep 4040
    (Not all processes could be identified, non-owned process info
    will not be shown, you would have to be root to see it all.)
    tcp6       0      0 :::4040                 :::*                    LISTEN      -  
    ```
    > 每一个Spark程序在运行的时候, 会绑定到Driver所在机器的4040端口上. <br/>
	如果4040端口被占用, 会顺延到4041...,可通过浏览器访问 4040端口

1. 通过spark-submit执行python脚本
    ```bash
	#官方脚本执行
	bin/spark-submit /export/server/spark/examples/src/main/python/pi.py 10

	#自定义脚本执行
	bin/spark-submit /export/demo/helloworld.py 
    hello,world!
    ```

## `PySpark`库安装

```bash
#创建虚拟环境
conda create -n pyspark python=3.9 

#切换虚拟环境
conda activate pyspark 

# 查看python
type python => python is /export/server/anaconda3/envs/pyspark/bin/python

# 编辑PYSPARK_PYTHON环境变量对应的值
vi /etc/profile
PYSPARK_PYTHON=/export/server/anaconda3/envs/pyspark/bin/python

# 安装pyspark
pip install pyspark -i https://pypi.tuna.tsinghua.edu.cn/simple

# 验证PySpark
python
>>> import pyspark #不报错则安装成功
```

## 本地开发环境搭建
> vscode + 远程解释器 + 远程代码
1. 密码登录服务器配置: 将windows本地的公钥配置在linux服务器`$HOME/.ssh/authorized_keys`中
1. vscode安装`remote development`插件,重启vscode
1. 添加远程ssh targets
	1. 点击ssh targets "+"
	1. 弹出框输入 ssh <linux username>@<your ip address>回车
	1. 选择 C:\\Users\\xxx\\.ssh\\config
	1. 编辑config文件
	```
	Host xxx
	HostName xxx
	User xxx
	ForwardAgent yes
	IdentityFile C:\\Users\\xxx\\.ssh\\id_rsa
	```
1. vscode安装python插件
1. 添加远程python解释器
	1. Ctrl + Shift + p打开命令面板
	1. 输入`Python: Select Interpreter`选择解释器
	1. 首次选择的是`/export/server/anaconda3/envs/pyspark/bin/python`
1. 编写helloworld.py代码
1. 执行（使用远程解释器)
1. 提升缺少package,安装python包`pip install jupyter notebook -i https://pypi.tuna.tsinghua.edu.cn/simple`
1. 运行成功

## spark安装(windows)

1. jdk安装(1.8)
2. 下载`spark-3.2.1-bin-hadoop2.7.zip`,`hadoop-2.7.7.zip`
3. 解压至`D:\export\server\`目录下
4. 下载`winutils.exec`放置在`hodoop-2.7.7\bin\`目录下
5. 环境变量配置`SPARK_HOME=D:\export\server\spark-3.2.1-bin-hadoop2.7`,`HADOOP_HOME=D:\export\server\hadoop-2.7.7`
6. 修改PATH环境变量配置添加`%SPARK_HOME%\bin`
7. 配置`PYSPARK_PYTHON=C:\Users\DELL\AppData\Local\Programs\Python\Python310\python.exe`(否则报错`: org.apache.spark.SparkException: Python worker failed to connect back`)

spark-submit --conf spark.sql.queryExecutionListeners="org.example.framework.LineageListener" --jars demo-scala-1.0-SNAPSHOT.jar E:\git\docs\bigdata\samples\pyspark\sparksql\test_lineage.py

<p style="color: #303f9f;"><b>In:</b></p>

```python
pyspark --packages io.delta:delta-core_2.12:2.1.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"

```
# PySpark版本查看

<p style="color: #303f9f;"><b>In:</b></p>

```python
import pyspark
pyspark.__version__

import os
os.environ
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
# Spark SQL(PySpark)

## Data Sources

### Generic Load/Save

#### load parquet

<p style="color: #303f9f;"><b>In:</b></p>

```python
import os

df = spark.read.load(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/users.parquet")
df.select("name", "favorite_color").write.mode('overwrite').save("spark_data/namesAndFavColors.parquet")
df.show()

df = spark.read.parquet(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/users.parquet")
(df.write.format("parquet")
    .option("parquet.bloom.filter.enabled#favorite_color", "true")
    .option("parquet.bloom.filter.expected.ndv#favorite_color", "1000000")
    .option("parquet.enable.dictionary", "true")
    .option("parquet.page.write-checksum.enabled", "false")
    .save("spark_data/users_with_options.parquet"))
```
#### load json

<p style="color: #303f9f;"><b>In:</b></p>

```python
df = spark.read.load(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.json", format="json")
df.select("name", "age").write.save("spark_data/namesAndAges.parquet", format="parquet")
df.show()
```
#### load csv

<p style="color: #303f9f;"><b>In:</b></p>

```python
df = spark.read.load(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.csv",
                     format="csv", sep=";", inferSchema="true", header="true")
df.show()
```
#### load orc

<p style="color: #303f9f;"><b>In:</b></p>

```python
df = spark.read.orc(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/users.orc")
t=(df.write.mode("overwrite").format("orc")
    .option("orc.bloom.filter.columns", "favorite_color")
    .option("orc.dictionary.key.threshold", "1.0")
    .option("orc.column.encoding.direct", "name")
    .save("spark_data/users_with_options.orc"))
df.show()
display(t)

# python () {} []中多行无需写 \
```
#### Run SQL on files directly

<p style="color: #303f9f;"><b>In:</b></p>

```python
df = spark.sql(f"SELECT * FROM parquet.`{os.environ['SPARK_HOME']}/examples/src/main/resources/users.parquet`")
df.show()
```
### Parquet Files

<p style="color: #303f9f;"><b>In:</b></p>

```python
df=spark.read.json(f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.json")
df.write.mode('overwrite').parquet('spark_data/people.parquet')

df=spark.read.parquet('spark_data/people.parquet')
df.printSchema()
df.show()

df.createOrReplaceTempView('parquetFile')
df=spark.sql('select name from parquetFile where age>=13 and age<=19')
df.show()
```
#### Schema Merging

<p style="color: #303f9f;"><b>In:</b></p>

```python
from pyspark.sql import Row

sc=spark.sparkContext

squaresDF=spark.createDataFrame(sc.parallelize(range(1,6)).map(lambda i:Row(single=i,double=i**2)))
squaresDF.show()
squaresDF.write.mode('overwrite').parquet('spark_data/test_table/key=1')

cubesDF=spark.createDataFrame(sc.parallelize(range(6,11)).map(lambda i:Row(single=i,triple=i**3)))
cubesDF.show()
cubesDF.write.mode('overwrite').parquet('spark_data/test_table/key=2')

mergedDF=spark.read.option('mergeSchema', 'true').parquet('spark_data/test_table')
mergedDF.printSchema()
mergedDF.show()
```
### Json Files
- the built-in functions below
    - from_json
    - to_json
    - schema_of_json

- data source option
    - primitivesAsString: true/false -- Infers all primitive values as a string
    - ignoreNullFields: true/false -- Whether to ignore null fields when generating JSON objects

<p style="color: #303f9f;"><b>In:</b></p>

```python
sc=spark.sparkContext
path=f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.json"
df=spark.read.json(path)
df.show()
df.printSchema()

jsonStrings=['{"name":"Yin","address":{"city":"columbus","state":"Ohio"}}']
rdd=sc.parallelize(jsonStrings)
df=spark.read.json(rdd)
df.show()
df.printSchema()
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
jsonStrings=['{"name":"Yin","address":{"city":"columbus","state":"Ohio"}, "number": 123 }']
rdd=sc.parallelize(jsonStrings)

df=spark.read.json(rdd) # `number` type is long
df.printSchema()
df.show()

df=spark.read.option('primitivesAsString', 'true').json(rdd) # `number` type is string
df.printSchema()
df.show()
```
### CSV Files
- built-in functions
    - from_csv
    - to_csv
    - schema_of_csv

<p style="color: #303f9f;"><b>In:</b></p>

```python
sc=spark.sparkContext
path=f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.csv"
df=spark.read.csv(path)
df.printSchema()
df.show()

# Read a csv with delimiter
df2=spark.read.option('delimiter', ';').csv(path) # delimiter default is ','
df2.printSchema()
df2.show()

# Read a csv with delimiter and a header
df3=spark.read.option('delimiter',';').option('header', True).csv(path)
df3=spark.read.options(delimiter=';', header=True).csv(path)
df3.printSchema()
df3.show()

df3.write.mode('overwrite').csv('spark_data/output')

# Wrong schema because non-CSV files are read
folderPath=f"{os.environ['SPARK_HOME']}/examples/src/main/resources"
df5=spark.read.csv(folderPath)
df5.printSchema()
df5.show()
```
### Text Files

<p style="color: #303f9f;"><b>In:</b></p>

```python
sc=spark.sparkContext
path=f"{os.environ['SPARK_HOME']}/examples/src/main/resources/people.txt"
df=spark.read.text(path)
df.printSchema()
df.show()

df=spark.read.text(path, lineSep=',')
df.printSchema()
df.show()

df=spark.read.text(path, wholetext=True)
df.printSchema()
df.show(truncate=False)

```
### JDBC To Other Databases

## Performance Tuning

### Caching Data In Memery
- spark.catalog.cacheTable('tableName')/spark.catalog.uncacheTable('tableName')
- dataFrame.cache()/dataFrame.unpersist()

### Join Strategy Hints for SQL Queries
