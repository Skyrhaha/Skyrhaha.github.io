# MongoDB
## 查询
- 查询name属性包含@的记录: {name: /@/}
- 日期比较查询 {runStart: {$lt: ISODate('2023-11-17')}}
- 按type字段分组: Compass进入->Aggregations,stage1选择$group,输入以下条件:
  ```
  {
    _id: null,
    type: {
      $addToSet: '$type'
    }
  }

  {
    _id: null,
    result-这里是结果字段名: {
      $addToSet: "$activity.typeProperties.source.type"
    }
  }
  ```
- 按字段分组统计
  ```
  {
    _id: "$properties.type",
    countOfType: {
      $count: {},
    },
  }
  ```


# ArangoDB
https://docs.python-arango.com/en/main/index.html
http://www.taodudu.cc/news/show-4225824.html?action=onClick
https://github.com/ArangoDB-Community/pyArango
