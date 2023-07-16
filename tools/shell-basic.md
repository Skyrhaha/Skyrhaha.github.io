# SHELL命令
## ls
```bash
#按K,M,G等为单位显示
ls -lh 

#类似ls -lh
du -sh * 
```

## find
```bash
# 查找大于1k大小的文件，友好显示，然后按大小倒序排序，取前10条
# -print0修改输出的分隔符为'\0'
# xargs -0指定分隔符为'\0'(xargs默认命令是echo)
find . -type f -size +1k -print0 | xargs -0 du -h | sort -nr|head -n10
```

## grep
```bash
# 在目录下的所有文件中搜索包含jdbc字符串的行
# -r 递归搜索目录下的文件
# -h 不显示文件名
grep -rh "jdbc" *

# 在文件中搜索不包含jdbc字符串的行
# -v 排除搜索
# -E 可以同时搜索多个字符串
grep -vE "jdbc|http" file.txt
```

## cut
```bash
# 按':'为分隔符进行列剪切并获取第一列(从1开始)
cut -d':' -f1 file.txt
```

## tr
```bash
# 去除换行符
cat file.txt|tr '\n' ''
```

## md5
```bash
# 生成md5
# md5sum filename
md5sum *.iso > file.md5

# 校验文件md5
md5sum -c file.md5
```

## zip加解密
```bash
# zip加密压缩
zip -rP pwd123 my.zip my.txt

# unzip解压
unzip -v my.zip #查看,不执行解压
unzip my.zip    #解压到当前
unzip -n my.zip -d /tmp  #解压到/tmp不覆盖
unzip -o my.zip -d /tmp  #解压到/tmp覆盖
unzip -P pwd123 my.zip   #使用密码解压
```

## while循环
```bash
# 每两秒查询一次网络LISTEN状态信息
while true; do netstat -an|grep LISTEN; sleep 2; done

grep xxx file.txt | awk -F':' '{print $1}'|uniq|while read line; do basename $line;done

while read line; do grep "$line" *.py; done < file.txt
```

## 立即执行`$()` vs ` `` `
```bash
$() vs `` : 执行命令
export PYTHONPATH=$(ZIPS=("$SPARK_HOME"/python/lib/*.zip); IFS=:; echo "${ZIPS[*]}"):$PYTHONPATH
```

# 场景使用

## 多行转换为一行
```bash
# 多行处理成一行(10个数字处理成一行带'[],'格式)
# seq 10 产生1-10数字，每个占一行
seq 10 | awk '{print "["$1"],"}' | xargs  # => [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],

# 多行转一行，并将每行用''包裹
seq 3 | awk '{print "'\''"$1"'\''"}' | tr "\n" "," # => '1','2','3'
```