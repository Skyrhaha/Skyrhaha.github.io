## linux安装
### linux node.js安装
```bash
wget https://nodejs.org/dist/v16.17.1/node-v16.17.1-linux-x64.tar.xz
tar Jxf node-v16.17.1-linux-x64.tar.xz

ln -s node-v16.17.1-linux-x64 node/
vi .bash_profile
export NODE_HOME=$HOME/setup/node
export PATH=$PATH:$NODE_HOME/bin

node -v
npm -v

# 修改源
npm config set registry https://registry.npm.taobao.org

# 查看配置
npm config list
```

### yarn安装
```bash
# yarn安装
npm install yarn -g

# 修改源
yarn config set registry https://registry.npm.taobao.org -g
yarn config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/ -g

# 检查配置
yarn config get registry // https://registry.npm.taobao.org
yarn config get sass_binary_site // https://npm.taobao.org/mirrors/node-sass/

# 基本操作
yarn init // 生成package.json文件
yarn install // 安装yarn.lock的所有依赖
yarn install --force // 重新安装依赖
yarn remove moduleName // 删除依赖
yarn add moduleName // 安装某个依赖
yarn add moduleName --dev/-D // 安装到开发环境
yarn run scriptName // 执行package.json命名的脚本命令
```

## windows安装
```bash
# 下载windows版node.js
https://nodejs.org/dist/v16.15.0/node-v16.15.0-x64.msi

# 双击安装

# 配置cache、prefix
npm config set cache "C:\setup\nodejs\node_cache"
npm config set prefix "C:\setup\nodejs\node_global"

# 环境变量设置
新增NODE_PATH=C:\setup\nodejs\node_global\node_modules
编辑Path环境变量，替换C:\Users\xxx\AppData\Roaming\npm为C:\setup\nodejs\node_global

# yarn安装
npm -g install yarn

# 报错处理
yarn -v报错：无法加载文件 C:\setup\nodejs\node_global\yarn.ps1，因为在此系统上禁止运行脚本
Admin 运行PowerShell输入set-ExecutionPolicy RemoteSigned，回车，选Y,回车

# 查看源
yarn config get registry
https://registry.yarnpkg.com

# 修改源
yarn config set registry=https://registry.npm.taobao.org
```