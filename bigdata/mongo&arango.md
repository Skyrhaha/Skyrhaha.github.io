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
  ```


# ArangoDB
https://github.com/ArangoDB-Community/pyArango
