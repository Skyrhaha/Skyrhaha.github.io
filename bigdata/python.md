# 参考资料
- 官方文档: https://docs.python.org/3/
- 此项目整理了各种应用场景下的python库信息: https://github.com/vinta/awesome-python
- 此项目整理了各种jupyerlab插件: https://github.com/mauhai/awesome-jupyterlab
- SparkSQL文档 https://spark.apache.org/docs/latest/sql-ref-functions.html
- Spark Structured Streaming文档 https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
- PySpark文档 https://spark.apache.org/docs/latest/api/python/index.html

# python基本命令

## python查看版本`python -V`

<p style="color: #303f9f;"><b>In:</b></p>

```python
!python -V
!python --version

import sys
sys.version
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
Python 3.10.7&#xA;Python 3.10.7&#xA;</pre>
<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
'3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)]'</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
!ipython3 notebook --version
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
8.5.0&#xA;</pre>
## 交互式修改提示符
1. 创建$HOME/.pythonstartup文件(python代码)
    ```python
    import sys

    sys.ps1=' '
    sys.ps2=' '
    ```
2. 编辑.bash_profile设置环境变量export PYTHONSTARTUP=~/.pythonstartup
3. python进入交互模式(提示符已修改)

<p style="color: #303f9f;"><b>In:</b></p>

```python
import sys
sys.ps1
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
'In : '</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
sys.ps2
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
'...: '</pre>
## 包安装`pip install <package-name>`

<p style="color: #303f9f;"><b>In:</b></p>

```python
!pip install pandas
!pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```
## 查看安装包信息`pip show <package-name>`

<p style="color: #303f9f;"><b>In:</b></p>

```python
!pip show jupyterlab
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
Name: jupyterlab&#xA;Version: 3.5.2&#xA;Summary: JupyterLab computational environment&#xA;Home-page: https://jupyter.org&#xA;Author: Jupyter Development Team&#xA;Author-email: jupyter@googlegroups.com&#xA;License: &#xA;Location: c:\users\dell\appdata\local\programs\python\python310\lib\site-packages&#xA;Requires: ipython, jinja2, jupyter-core, jupyter-server, jupyterlab-server, nbclassic, notebook, packaging, tomli, tornado&#xA;Required-by: ipydrawio, jupyterlab-drawio&#xA;</pre>
## 查看所有已安装的包`pip list`

<p style="color: #303f9f;"><b>In:</b></p>

```python
!pip list
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
import sys
sys.path
```
# 基础操作

## r 忽略反斜杠`\`

## `*`与`**`
- `*`: 余参收集
- `**`: 关键字余参收集

<p style="color: #303f9f;"><b>In:</b></p>

```python
def fun1(*params):
    print(params)

fun1(1, 'b', 3)

p=(1,2,3)
fun1(*p)

def fun2(**params):
    print(params)

fun2(a=1,b=2,c=3)

def fun3(a, b, c):
    print(f"a={a} b={b} c={c}")
p={'a': 'aa', 'b': 2, 'c': 'cc'}
fun3(**p)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
(1, 'b', 3)&#xA;(1, 2, 3)&#xA;{'a': 1, 'b': 2, 'c': 3}&#xA;a=aa b=2 c=cc&#xA;</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
def myfun(*params, k1='', k2=''):
    print(f"{params=}")
    print(list(params))
    print(str(params), len(params))
    # p = *params
    # print(p, type(p))
    print(f"{k1=}")
    print(f"{k2=}")
    
myfun('a', 'b', 'c', k1='aa', k2='bb')
myfun('aaa','bbb')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
params=('a', 'b', 'c')&#xA;['a', 'b', 'c']&#xA;('a', 'b', 'c') 3&#xA;k1='aa'&#xA;k2='bb'&#xA;params=('aaa', 'bbb')&#xA;['aaa', 'bbb']&#xA;('aaa', 'bbb') 2&#xA;k1=''&#xA;k2=''&#xA;</pre>
## 属性删除del <attribute>

<p style="color: #303f9f;"><b>In:</b></p>

```python
class Demo:
    a=1
    b=1

print(dir(Demo))
del Demo.a
print(dir(Demo))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b']&#xA;['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'b']&#xA;</pre>
## global vs nonlocal
- global在函数里声明使用全局变量
- nonlocal使用介于全局变量(不是全局变量)与局部变量之间

<p style="color: #303f9f;"><b>In:</b></p>

```python
def scope_test():
    def do_local():
        spam='local spam'
        
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    
    def do_global():
        global spam
        spam = 'global spam'
    
    spam = 'test spam'
    
    do_local()
    print(f'after do_local {spam=}')
    
    do_nonlocal()
    print(f'after do_nonlocal {spam=}')
    
    do_global()
    print(f'after do_global {spam=}')

scope_test()
print(f"i'm global {spam=}")
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
after do_local spam='test spam'&#xA;after do_nonlocal spam='nonlocal spam'&#xA;after do_global spam='nonlocal spam'&#xA;i'm global spam='global spam'&#xA;</pre>
## stepping

<p style="color: #303f9f;"><b>In:</b></p>

```python
a=[1,2,3,4,5]

print(a[::2])
print(a[::-1])

[ print(i) for i in iter(a) ]
a=iter(a)
next(a)
next(a)
next(a)
next(a)
next(a)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
[1, 3, 5]&#xA;[5, 4, 3, 2, 1]&#xA;1&#xA;2&#xA;3&#xA;4&#xA;5&#xA;</pre>
<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
5</pre>
## is not

<p style="color: #303f9f;"><b>In:</b></p>

```python
a='abc'

if a is not True:
    print('a is not True')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
a is not True&#xA;</pre>
# built-in function

<p style="color: #303f9f;"><b>In:</b></p>

```python
arr=[0,1,2,3]
print(f"{all(arr)=}")
print(f"{any(arr)=}")

print(f"{ascii('abc')=}")

print(f"{bin(11)=}")
print(f"{format(11,'#b')=}")
print(f"{format(11,'b')=}")

print(f"{bool(1)=} {bool(0)=} {bool(2)=}")

seasons = ['a','b','c']
print(list(enumerate(seasons,start=1)))

x=10
r=eval('x+1')
r

arr=[1,3,2,9]
[ e for e in arr if e <3 ]
print(list(filter(lambda x: x<3, arr)))
print([e for e in filter(lambda x: x<3, arr)])
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
all(arr)=False&#xA;any(arr)=True&#xA;ascii('abc')="'abc'"&#xA;bin(11)='0b1011'&#xA;format(11,'#b')='0b1011'&#xA;format(11,'b')='1011'&#xA;bool(1)=True bool(0)=False bool(2)=True&#xA;[(1, 'a'), (2, 'b'), (3, 'c')]&#xA;[1, 2]&#xA;[1, 2]&#xA;</pre>
## dir() 查看模块定义的所有名字
- dir(moduleName) 查看指定模块
- dir() 查看当前模块
- dir()不列出built-in内容,built-in使用dir(builtins)查看

<p style="color: #303f9f;"><b>In:</b></p>

```python
dir(sys)
dir()

import string
dir(string)

import builtins
dir(builtins)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
['ArithmeticError',&#xA; 'AssertionError',&#xA; 'AttributeError',&#xA; 'BaseException',&#xA; 'BlockingIOError',&#xA; 'BrokenPipeError',&#xA; 'BufferError',&#xA; 'BytesWarning',&#xA; 'ChildProcessError',&#xA; 'ConnectionAbortedError',&#xA; 'ConnectionError',&#xA; 'ConnectionRefusedError',&#xA; 'ConnectionResetError',&#xA; 'DeprecationWarning',&#xA; 'EOFError',&#xA; 'Ellipsis',&#xA; 'EncodingWarning',&#xA; 'EnvironmentError',&#xA; 'Exception',&#xA; 'False',&#xA; 'FileExistsError',&#xA; 'FileNotFoundError',&#xA; 'FloatingPointError',&#xA; 'FutureWarning',&#xA; 'GeneratorExit',&#xA; 'IOError',&#xA; 'ImportError',&#xA; 'ImportWarning',&#xA; 'IndentationError',&#xA; 'IndexError',&#xA; 'InterruptedError',&#xA; 'IsADirectoryError',&#xA; 'KeyError',&#xA; 'KeyboardInterrupt',&#xA; 'LookupError',&#xA; 'MemoryError',&#xA; 'ModuleNotFoundError',&#xA; 'NameError',&#xA; 'None',&#xA; 'NotADirectoryError',&#xA; 'NotImplemented',&#xA; 'NotImplementedError',&#xA; 'OSError',&#xA; 'OverflowError',&#xA; 'PendingDeprecationWarning',&#xA; 'PermissionError',&#xA; 'ProcessLookupError',&#xA; 'RecursionError',&#xA; 'ReferenceError',&#xA; 'ResourceWarning',&#xA; 'RuntimeError',&#xA; 'RuntimeWarning',&#xA; 'StopAsyncIteration',&#xA; 'StopIteration',&#xA; 'SyntaxError',&#xA; 'SyntaxWarning',&#xA; 'SystemError',&#xA; 'SystemExit',&#xA; 'TabError',&#xA; 'TimeoutError',&#xA; 'True',&#xA; 'TypeError',&#xA; 'UnboundLocalError',&#xA; 'UnicodeDecodeError',&#xA; 'UnicodeEncodeError',&#xA; 'UnicodeError',&#xA; 'UnicodeTranslateError',&#xA; 'UnicodeWarning',&#xA; 'UserWarning',&#xA; 'ValueError',&#xA; 'Warning',&#xA; 'WindowsError',&#xA; 'ZeroDivisionError',&#xA; '__IPYTHON__',&#xA; '__build_class__',&#xA; '__debug__',&#xA; '__doc__',&#xA; '__import__',&#xA; '__loader__',&#xA; '__name__',&#xA; '__package__',&#xA; '__spec__',&#xA; 'abs',&#xA; 'aiter',&#xA; 'all',&#xA; 'anext',&#xA; 'any',&#xA; 'ascii',&#xA; 'bin',&#xA; 'bool',&#xA; 'breakpoint',&#xA; 'bytearray',&#xA; 'bytes',&#xA; 'callable',&#xA; 'chr',&#xA; 'classmethod',&#xA; 'compile',&#xA; 'complex',&#xA; 'copyright',&#xA; 'credits',&#xA; 'delattr',&#xA; 'dict',&#xA; 'dir',&#xA; 'display',&#xA; 'divmod',&#xA; 'enumerate',&#xA; 'eval',&#xA; 'exec',&#xA; 'execfile',&#xA; 'filter',&#xA; 'float',&#xA; 'format',&#xA; 'frozenset',&#xA; 'get_ipython',&#xA; 'getattr',&#xA; 'globals',&#xA; 'hasattr',&#xA; 'hash',&#xA; 'help',&#xA; 'hex',&#xA; 'id',&#xA; 'input',&#xA; 'int',&#xA; 'isinstance',&#xA; 'issubclass',&#xA; 'iter',&#xA; 'len',&#xA; 'license',&#xA; 'list',&#xA; 'locals',&#xA; 'map',&#xA; 'max',&#xA; 'memoryview',&#xA; 'min',&#xA; 'next',&#xA; 'object',&#xA; 'oct',&#xA; 'open',&#xA; 'ord',&#xA; 'pow',&#xA; 'print',&#xA; 'property',&#xA; 'range',&#xA; 'repr',&#xA; 'reversed',&#xA; 'round',&#xA; 'runfile',&#xA; 'set',&#xA; 'setattr',&#xA; 'slice',&#xA; 'sorted',&#xA; 'staticmethod',&#xA; 'str',&#xA; 'sum',&#xA; 'super',&#xA; 'tuple',&#xA; 'type',&#xA; 'vars',&#xA; 'zip']</pre>
## isinstance(obj, `<type>`)

<p style="color: #303f9f;"><b>In:</b></p>

```python
class D:
    pass

class C(D):
    pass

c=C()
print(isinstance(c, D))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
True&#xA;</pre>
## issubclass(`<subtype>`,`<type>`)

<p style="color: #303f9f;"><b>In:</b></p>

```python
print(issubclass(C,D))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
True&#xA;</pre>
## enumerate(iterable, start=0)

<p style="color: #303f9f;"><b>In:</b></p>

```python
seasons=['Spring', 'Summer', 'Fall', 'Winter']
for i,v in enumerate(seasons):
    print(i,v)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
0 Spring&#xA;1 Summer&#xA;2 Fall&#xA;3 Winter&#xA;</pre>
## zip(*iterables, strict=False)

<p style="color: #303f9f;"><b>In:</b></p>

```python
questions=['name', 'quest', 'favorite color']
answers=['lancelot', 'the holy grail', 'blue']

for q,a in zip(questions, answers):
    print(q,a)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
name lancelot&#xA;quest the holy grail&#xA;favorite color blue&#xA;</pre>
# Modules

<p style="color: #303f9f;"><b>In:</b></p>

```python
import fibo

fibo.__name__

fibo.fib(10)
fibo.fib2(10)

dir(fibo)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
0 1 1 2 3 5 8 </pre>
<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
['__builtins__',&#xA; '__cached__',&#xA; '__doc__',&#xA; '__file__',&#xA; '__loader__',&#xA; '__name__',&#xA; '__package__',&#xA; '__spec__',&#xA; 'fib',&#xA; 'fib2']</pre>
## 模块查找规则
- 先在build-in模块查找
- 然后在sys.path的目录下查找,sys.path is initialized form these locations:
    - the directory containing the input script/or the current directory when no file is specified
    - PYTHONPATH(a list of directory names,with the same syntax as the shell variable PATH)
    - the installation-dependent default(by convention including a `site-packages` directory,handled by the site module)
- sys.path.append修改sys.path

<p style="color: #303f9f;"><b>In:</b></p>

```python
import sys
import os

# show built-in modules
sys.builtin_module_names

sys.path

os.getenv('PYTHONPATH','not set')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
'not set'</pre>
# Errors and Exceptions

<p style="color: #303f9f;"><b>In:</b></p>

```python
import sys

try :
    f=open('fibo.py')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print('OS error:', err)
# except ValueError as err:
#     print('Value error:', err)
except Exception as err:
    print(f'Unexcepted {err=}, {type(err)=}')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
Unexcepted err=ValueError("invalid literal for int() with base 10: 'def fib(n):'"), type(err)=&lt;class 'ValueError'>&#xA;</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
raise NameError
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="background: #fddfdd; padding-top: 5px">
---------------------------------------------------------------------------&#xA;NameError                                 Traceback (most recent call last)&#xA;Cell In [10], line 1&#xA;----> 1 raise NameError&#xA;&#xA;NameError: </pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
raise NameError('name error')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="background: #fddfdd; padding-top: 5px">
---------------------------------------------------------------------------&#xA;NameError                                 Traceback (most recent call last)&#xA;Cell In [11], line 1&#xA;----> 1 raise NameError('name error')&#xA;&#xA;NameError: name error</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
try:
    f=open('my.txt')
except OSError as err:
    raise
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="background: #fddfdd; padding-top: 5px">
---------------------------------------------------------------------------&#xA;FileNotFoundError                         Traceback (most recent call last)&#xA;Cell In [9], line 2&#xA;      1 try:&#xA;----> 2     f=open('my.txt')&#xA;      3 except OSError as err:&#xA;      4     raise&#xA;&#xA;FileNotFoundError: [Errno 2] No such file or directory: 'my.txt'</pre>
# Classes

## 类定义 

<p style="color: #303f9f;"><b>In:</b></p>

```python
class MyClass:
    """class MyClass"""

    # 私有属性，只能在类内部使用
    __version='1.0'
    
    i=1
    
    # 魔法方法: 构造方法
    def __init__(self):
        self.data=[]

    # 私有方法,只能在类内部使用
    def __version(self):
        print(f"version: {self.__version}")
        
    def f(self):
        print('do f')

print(dir(MyClass))
print(f'{MyClass.__doc__=}')

x=MyClass()
print(dir(x))

# data attributes 无需定义
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(f"{x.counter=}")
del x.counter

# x.f() vs MyClass.f(x)
x.f()
MyClass.f(x)

# class variable vs instance variable
class Dog:
    kind='kind' # class variable

    def __init__(self,name=''):
        self.name=name

d1=Dog('a')
d2=Dog('b')
print(f"{d1.kind=} {d2.kind=} {d1.name=} {d2.name=}")
print(d1.__class__)

print(isinstance(d1, Dog))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
['_MyClass__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'f', 'i']&#xA;MyClass.__doc__='class MyClass'&#xA;['_MyClass__version', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data', 'f', 'i']&#xA;x.counter=16&#xA;do f&#xA;do f&#xA;d1.kind='kind' d2.kind='kind' d1.name='a' d2.name='b'&#xA;&lt;class '__main__.Dog'>&#xA;True&#xA;</pre>
<p style="color: #303f9f;"><b>In:</b></p>

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

e=Employee('A', 'DD', 100)
print(f"{e.name=} {e.dept=} {e.salary=}")

```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
e.name='A' e.dept='DD' e.salary=100&#xA;</pre>
<pre style="background: #fddfdd; padding-top: 5px">
---------------------------------------------------------------------------&#xA;AttributeError                            Traceback (most recent call last)&#xA;Cell In [56], line 11&#xA;      9 e=Employee('A', 'DD', 100)&#xA;     10 print(f"{e.name=} {e.dept=} {e.salary=}")&#xA;---> 11 print(e.__func__)&#xA;&#xA;AttributeError: 'Employee' object has no attribute '__func__'</pre>
## 多继承

<p style="color: #303f9f;"><b>In:</b></p>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"name={self.name} age={self.name}")

class Father(Person):
    def work(self):
        print(f"{self.name} working...")

class Mother(Person):
    def shopping(self):
        print(f"{self.name} shopping...")

class Child(Father,Mother,Person):
    def __init__(self, fname,fage,mname,mage, name, age):
        Father.__init__(self, fname,fage)
        Mother.__init__(self, mname,mage)
        Person.__init__(self,name,age)

child=Child('fname', 40, 'mm', 35, 'child', 10)
child.show()
child.work()
child.shopping()
print(child.name)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
name=child age=child&#xA;child working...&#xA;child shopping...&#xA;child&#xA;</pre>
### 父类调用
- 方式一: super().父类方法()
- 方式二: 父类.父类方法(self,...)

## 类型注解

<p style="color: #303f9f;"><b>In:</b></p>

```python
# 变量类型注解
var1: int = 0
print(type(var1))

# 对形参进行类型注解,对函数的返回值进行类型注解
def add(x:int, y:int) -> int:
    return x+y

add(1,2)

# Union类型注解
from typing import Union

my_list: list[Union[str,int]] = [1,2,'test']
print(type(my_list))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
&lt;class 'int'>&#xA;&lt;class 'list'>&#xA;</pre>
## 多态

<p style="color: #303f9f;"><b>In:</b></p>

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("wang wang")

class Cat(Animal):
    def speak(self):
        print("miao miao")
        
def make_noise(a: Animal):
    a.speak()

dog=Dog()
cat=Cat()
make_noise(dog)
make_noise(cat)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
wang wang&#xA;miao miao&#xA;</pre>
# 高级特性

## 闭包

### 使用global全局变量
- 代码不够干净
- 存在全局变量被篡改的风险

<p style="color: #303f9f;"><b>In:</b></p>

```python
count=0

def counter():
    global count
    # count=-1
    
    count += 1

counter()
counter()
counter()
print(f"count={count}")
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
count=3&#xA;</pre>
### 闭包实现

<p style="color: #303f9f;"><b>In:</b></p>

```python
def outer_func(count):
    def inner_func():
        nonlocal count
        count += 1
        return count
    
    return inner_func

fn=outer_func(3)
fn()
fn()
print(fn())
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
6&#xA;</pre>
## 装饰器

<p style="color: #303f9f;"><b>In:</b></p>

```python
def outer(func):
    def inner():
        print("before ...")
        func()
        print("after ...")
    return inner

@outer
def bizfun():
    print("biz process...")

bizfun()
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
before ...&#xA;biz process...&#xA;after ...&#xA;</pre>
### 带参数装饰器

<p style="color: #303f9f;"><b>In:</b></p>

```python
def mylog(param):
    def wraper(func):
        def inner(*args, **kwargs):
            print(f"param={param} wraper before...")
            print(f"exec {func.__name__}...")
            func(*args, **kwargs)
            print(f"param={param} wraper after...")
        return inner
    return wraper

@mylog('xxx')
def bizfun2():
    print("bizfun2 process...")
    
bizfun2()
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
param=xxx wraper before...&#xA;exec bizfun2...&#xA;bizfun2 process...&#xA;param=xxx wraper after...&#xA;</pre>
### 函数装饰器封装进类

<p style="color: #303f9f;"><b>In:</b></p>

```python
class HiDecorate:
    def info(self,func):
        print(f"exec {func.__name__} ...")
        return func()
    
    def argsinfo(self,func):
        def wrap(*args):
            print(f"exec {func.__name__},args:{args}")
            return func(*args)
        return wrap
    
decorate=HiDecorate()

@decorate.info
def f():
    print("hi decorate")

# f() # 直接调用报错

@decorate.argsinfo
def f2(a,b):
    print('f2 hi decrote')
f2(1,2)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
exec f ...&#xA;hi decorate&#xA;exec f2,args:(1, 2)&#xA;f2 hi decrote&#xA;</pre>
### functools.wraps
- 还原因装饰器导致的__name__属性被修改为wrapper的__name__

<p style="color: #303f9f;"><b>In:</b></p>

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper1():
        s=time.time()
        func()
        e=time.time()
        print(f"exec [{func.__name__}] spent {e-s}s")
    return wrapper1

@timer
def test():
    time.sleep(1)

test()
print(test.__name__)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
exec [test] spent 1.0009815692901611s&#xA;test&#xA;</pre>
### 类装饰器

<p style="color: #303f9f;"><b>In:</b></p>

```python
import time

class Timer():
    def __init__(self, func):
        self.func=func
        self.__name__=func.__name__
        
    def __call__(self):
        s=time.time()
        self.func()
        e=time.time()
        print(f"exec [{self.func.__name__}] spent {e-s}s")  

@Timer # 等价于 test2=Timer(func)
def test2():
    time.sleep(1)

test2()
print(test2.__name__)
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
exec [test2] spent 1.0057063102722168s&#xA;test2&#xA;</pre>
### `__call__`
- magic method
- 作用是把一个类的实例化对象变成可调用的对象
- 使用callable(obj)可检测对象是否可以被调用

<p style="color: #303f9f;"><b>In:</b></p>

```python
class P1:
    pass

p1=P1()
print(callable(p1))
# p1()

class P2:
    def __call__(self):
        print('我是可以被调用的P2实例')

p2=P2()
print(callable(p2))
p2()
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
False&#xA;True&#xA;我是可以被调用的P2实例&#xA;</pre>
## 设计模式

### 单例模式
- 将需要单例模式的类放在独立的文件中并实例化一个对象
- 其它使用的地方通过 `from <单例模块> import <单例对象>`的方式使用即为单例模式
```python
# 单例.py
class SS:
    pass

s=SS()

# ref.py
from 单例 import s

a=s
b=s

```

<p style="color: #303f9f;"><b>In:</b></p>

```python
class S1:
    pass

s1=S1()
s2=S1()

print(f"s1={id(s1)} s2={id(s2)}")
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
s1=1660063275696 s2=1660043121168&#xA;</pre>
### 工厂模式

## 并发编程
 - python对并发编程的支持
    - 多线程 threading,利用CPU和IO可以同时执行原理
    - 多进程 multiprocessing,利用多核CPU真正的并行执行
    - 异步IO asyncio, 在单线程利用CPU和IO同时执行的原来，实现函数异步执行
    - 使用Lock对资源进行加锁
    - 使用Queue事项不同线程/进程间数据通信,实现生产者-消费者模式
    - 使用线程池Pool/进程池Pook
    - 使用subprocess启动外部程序的进程，并进行输入输出交互
- 怎么选择多线程/多进程/多协程?
    - 单线程
    - 多线程 threading,利用CPU和IO可以同时执行原理
    - 多CPU并行 multiprocessing,利用多核CPU真正的并行执行
    - 多机器并行 spark等
- CPU密集型 vs I/O密集型
    - CPU密集型(CPU bound): 也叫计算密集型，是指I/O在很短的时间完成，CPU需要大量的计算和处理,特点是CPU占用率高;如压缩解压缩、加密解密、正则表达式搜索
    - IO密集型(I/O bound):是系统运作大部分的状况是CPU在等待I/O(内存/硬盘)的读/写,CPU占用率较低;如文件处理、网络爬虫、读写数据库
- Thread/Process/Coroutine
    - 多线程Thread(threading)
        - 相比进程: python多线程只能并发执行，不能利用多CPU(GIL)
        - 相比协程: 有线程开销
    - 多进程Process(multiprocessing)
    - 多协程Coroutine(asyncio)
        - 支持库有限制(如requests不支持)
- 对比选择
任务特点|选择|
 -- | -- |
任务为CPU密集型 | 多进程 |
任务I/O密集型，不需要超多任务 | 多线程 |
任务I/O密集型，需要超多任务 | 多协程 |

### GIL (Global Interpreter Lock)
全局解释器锁: 是计算机程序设计语言解释器用于同步线程的一种机制，它使得任何时刻仅有一个线程在执行,即使在多核处理器上，使用GIL的解释器也只允许同一时间执行一个线程
- When a thread is running,it holds the GIL
- GIL released on I/O(read,write,send,recv,etc.)
- 参考: http://www.dabeaz.com/python/UnderstandingGIL.pdf

### 示列-多线程

<p style="color: #303f9f;"><b>In:</b></p>

```python
import requests
import time

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1,50+1)
]
print(urls)

def craw(url):
    r = requests.get(url)
    print(url, len(r.text))
    
# craw(urls[0])

def single_thread():
    print("single_thread begin...")
    for url in urls:
        craw(url)

import threading

def multi_thread():
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))
        )
        
    for t in threads:
        t.start()
    for t in threads:
        t.join()

# single_thread()
multi_thread()
```
### 示例-producer/counsumer
- 多组建的pipeline技术架构
- 多线程数据通信queue.Queue: 线程安全
    - import queue
    - 创建 q=queue.Queue()
    - 添加 q.put(item)
    - 读取 q.get(item)
    - 查看元素多少 q.qsize()
    - 判空 q.empty()
    - 判断是否已满 q.full()

<p style="color: #303f9f;"><b>In:</b></p>

```python
import queue
import requests
import time
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1,50+1)
]
# print(urls)

def craw(url):
    r = requests.get(url)
    # print(url, len(r.text))
    return r.text

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all("a", class_="post-item-title")
    return [ (link["href"], link.get_text()) for link in links ]

for e in parse(craw(urls[2])):
    print(e)

    
import queue
import time
import random
import threading

def do_craw(url_queue:queue.Queue, html_queue: queue.Queue):
    while True:
        url=url_queue.get()
        html = craw(url)
        html_queue.put(html)
        
        print(f"thread name={threading.current_thread().name} url={url} url_queue size={url_queue.qsize()}")
        time.sleep(random.randint(1,2))
        
def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        res = parse(html)
        for e in res:
            fout.write(str(e) + "\n")
            
        print(f"thread name={threading.current_thread().name} url={url} html_queue size={html_queue.qsize()}")
        time.sleep(random.randint(1,2))
        

url_queue = queue.Queue()
html_queue = queue.Queue()
for url in urls:
    url_queue.put(url)

for idx in range(3):
    t=threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
    t.start()

fout = open("data/craw.data.txt","w")
for idx in range(2):
    t=threading.Thread(target=do_parse,args=(html_queue,fout), name=f"parse{idx}")
    t.start()
```
### 示例-Lock用于解决线程安全
- try-finally模式
```python
import threading
lock=threading.Lock()
lock.acquire()

try:
    # do something
finally:
    lock.release()
```

- with模式
```python
import threading

lock = threading.Lock()
with lock:
    # do something
```

## 字节码
- 查看字节码 dis.dis(x)
- code object介绍

# 库

## os

<p style="color: #303f9f;"><b>In:</b></p>

```python
import os

print(os.getcwd())
os.system('ls -l')
dir(os)
help(os)
```
## shutil

<p style="color: #303f9f;"><b>In:</b></p>

```python
import shutil

help(shutil)
```
## glob

<p style="color: #303f9f;"><b>In:</b></p>

```python
import glob
print(glob.glob('*.py'))
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
['fibo.py']&#xA;</pre>
## string
### Template模板字符串

<p style="color: #303f9f;"><b>In:</b></p>

```python
from string import Template

t=Template('hello, ${name}')
t.substitute(name='xx')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
'hello, xx'</pre>
## logging
- https://stackoverflow.com/questions/18786912/get-output-from-the-logging-module-in-ipython-notebook

<p style="color: #303f9f;"><b>In:</b></p>

```python
import logging
import importlib

importlib.reload(logging)

print(type(logging.INFO))
print(logging.INFO)

logging.basicConfig(level=logging.INFO)

importlib.reload(logging)
logging.basicConfig(format='%(asctime)s |%(levelname)8s|%(filename)s:%(lineno)d|%(funcName)s| %(message)s',
                    level=logging.DEBUG, 
                    datefmt='%y-%m-%d %H:%M:%S',
                    stream=sys.stdout)

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('warning: config file %s not found!', 'server.conf')
logging.error('error')
logging.critical('critical error -- shutting down')

def func():
    logging.info('funcName test')

func()
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
&lt;class 'int'>&#xA;20&#xA;23-04-15 15:41:50 |   DEBUG|1157483613.py:17|&lt;module>| Debugging information&#xA;23-04-15 15:41:50 |    INFO|1157483613.py:18|&lt;module>| Informational message&#xA;23-04-15 15:41:50 | WARNING|1157483613.py:19|&lt;module>| warning: config file server.conf not found!&#xA;23-04-15 15:41:50 |   ERROR|1157483613.py:20|&lt;module>| error&#xA;23-04-15 15:41:50 |CRITICAL|1157483613.py:21|&lt;module>| critical error -- shutting down&#xA;23-04-15 15:41:50 |    INFO|1157483613.py:24|func| funcName test&#xA;</pre>
## smtplib
https://www.runoob.com/python3/python3-smtp.html

## apscheduler
- 任务调度
- 类似有schedule,celery
- 文档 https://apscheduler.readthedocs.io/en/3.x/userguide.html
- github https://github.com/agronholm/apscheduler/tree/3.x/examples/?at=master

### basic concepts
APScheduler has four kinds of components
- triggers
- job stores
- executors
- schedulers

### 选择
- scheduler: BlockingScheduler vs BackgroundScheduler
- trigger: date, interval, cron
- jobstore: memery vs persist(db)
- executor: ThreadPoolExecutor vs ProcessPoolExecutor


<p style="color: #303f9f;"><b>In:</b></p>

```python
pip install apscheduler
```
### 示列

<p style="color: #303f9f;"><b>In:</b></p>

```python
import time
import json
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime

def myjob():
    event={
        'taskId': 'sc export'
    }
    print(f"send event : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {json.dumps(event)}...")
    
# bs=BlockingScheduler()
bs=BackgroundScheduler()
trigger=IntervalTrigger(seconds=5)
bs.add_job(myjob, trigger)

bs.start()

print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        print("sleep...")
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    print("bs shutdown...")
    # Not strictly necessary if daemonic mode is enabled but should be done if possible
    bs.shutdown()
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
bs.shutdown()
```
<p style="color: #303f9f;"><b>In:</b></p>

```python
from apscheduler.triggers.cron import CronTrigger

CronTrigger.from_crontab('0 0 1-15 may-aug *')
```
<p style="color: #d84315;"><b>Out:</b></p>

<pre style="overflow-x:auto; background: #eaeef2; padding-top: 5px">
&lt;CronTrigger (month='may-aug', day='1-15', day_of_week='*', hour='0', minute='0', timezone='Asia/Shanghai')></pre>