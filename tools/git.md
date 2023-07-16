## 介绍
- [入门指南-菜鸟教程](https://www.runoob.com/manual/git-guide/)
- [git教程-菜鸟教程](https://www.runoob.com/git/git-workspace-index-repo.html)

## 参数配置
```bash
# 配置用户信息
git config --global user.name "your usernmae"
git config --global user.email "your email"

# 查看配置信息
git config --list

# 服务器配置好SSH公钥后客户端输入以下语句可只在首次需要输入用户名密码
git config --global credential.helper store
```

## 常用命令
```bash
# 检出远程仓库
git clone username@host:/path/to/repository

# 添加工作空间(workspace)文件到暂存区(Index/Stage)
git add <filename>
git add .

# 提交暂存区(Index/Stage)修改到本地版本库(local repository)
git commit -m "修改信息"

# 合并feature_x分支到当前分支(如master)
git merge feature_x # 当前为master分支

# 同步远程仓库到工作空间(workspace)
git pull 

# 推送本地版本库(local repository)修改到远程仓库(remote repoitory)
git push origin master # master可以替换为想提交的其它分支

# 本地分支查看与切换
git branch # 查看分支
git checkout feature_x # 切换为feature_x分支

# 当前状态查看
git status

# 提交信息查看
git log
git log --oneline
git log --graph
git blame <file> # 查看单个文件修改记录

# remote操作
git remote -v #查看remote信息
git remote rm origin #删除remote origin
git remote add origin repo #关联远程仓库
```

## 标签管理
```bash
# 查看tag信息
git tag -n

# 切换tag
git checkout <tag_name>
```

## 仓库迁移
```bash
# 从原地址克隆一份裸版本库
git clone --bare username@host:/path/to/old_repo

# 然后到新的git服务器上创建一个新项目，如new_repo

# 以镜像推送的方式上传代码到new_repo服务器上
cd /path/to/old_repo
git push --mirror username@host:/path/to/new_repo

# 删除本地代码
cd ..
rm -rf old_repo

# 重新clone new_repo
git clone username@host:/path/to/new_repo
```

## 分支管理规范
## 提交信息规范