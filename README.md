# MONITOR_BOT

## 基础信息
ProjectName | CreateDate | Author | ChineseName
--- | --- | --- | ---
monitor_bot | 2018-04-28 | TauWoo | 基于WebQQ,WebWechat协议的监控机器人

## 开发进度
### 1. **基础组件**
- [ ] 第三方依赖库qqbot封装 @TauWu
- [ ] 第三方依赖库wxpy封装  @TauWu
- [ ] HTTP请求封装
- [ ] 定时任务模块封装
- [ ] 数据库数据获取封装
- [ ] 文件配置模块封装
- [ ] 日志模块封装
- [ ] `待定`Redis缓存封装

### ２. **功能模块**
- [ ] 简易天气接口数据监控
- [ ] 简易天气接口数据定时任务
- [ ] 链家爬虫接口监控 @TauWu
- [ ] 安居客爬虫数据库监控 @TauWu
- [ ] `待定`爬虫Redis数据监控和定时任务 @TauWu

### 3. **待议模块**
- [ ] `待定`第三方游戏接口数据获取和主动消息触发
- [ ] `待定`第三方机器人接口接入
- [ ] `幻想`基于机器学习的智能聊天功能
- [ ] `幻想`基于Image的图片处理功能

## 部署说明
### 1.**系统支持**
- [x] Linux
> - [x] Ubuntu
> - [ ] CentOS
- [ ] Windows
- [ ] OSX

### 2.**依赖软件和依赖库安装**
- On Linux 
```sh
# 软件安装
apt-get install python3
apt-get install mysql-server
apt-get install redis-server
apt-get install python3-pip
apt-get install python-bs4

# Python依赖库
pip3 install requests
pip3 install PyMySQL
pip3 install redis
pip3 install configparser
pip3 install gevent
pip3 install qqbot
pip3 install wxpy
```

### 3.**目录结构**
目录名 | 介绍
:--- | ---
util | 工具代码
util/common | 通用基础工具
util/extension | 针对本项目的基础工具
module | 功能模块代码
module/logic | 逻辑处理代码
module/base | 基础操作代码
module/base/constant | 常量存放代码
module/base/db | 数据库操作代码
module/base/rds | Redis操作代码
module/base/web | 请求服务操作代码
module/extension | 工具性质代码
log | 日志模块输出
database | 数据库建表语句