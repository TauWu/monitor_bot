#!/usr/bin/python3
# -*- coding: utf-8 -*-

from util.common.config import ConfigParser

def default_config(key, value):
    return key

def get_config():
    
    # 数据库配置
    print("开始配置数据库...")
    db_host = input("请输入数据库的host（跳过为localhost）")
    db_user = input("请输入数据库的user（跳过为root）")
    db_port = input("请输入数据库的端口（跳过为3306）")
    db_pwd = input("请输入数据库的pwd（跳过为root）")
    db_db = input("请输入数据库的数据库名（跳过为monitor_bot）")

    if len(db_host) == 0:
        db_host = "127.0.0.1"
    if len(db_user) == 0:
        db_user = "root"
    if len(db_pwd) == 0:
        db_pwd = "root"
    if len(db_db) == 0:
        db_db = "monitor_bot"
    if len(db_port) == 0:
        db_port = "3306"
            
    # Redis配置
    # BasicInfo Redis
    print("开始配置Redis连接...")
    redis_host = input("请输入Redis的host（跳过为localhost）")
    if len(redis_host) == 0:
        redis_host = "127.0.0.1"
    redis_port = input("请输入Redis端口号（跳过为6379）")
    if len(redis_port) == 0:
        redis_port = "6379"
    redis_port = int(redis_port)
                    
    return dict(
        database=dict(host=db_host, user=db_user, passwd=db_pwd, db=db_db, port=db_port),
        redis = dict(host=redis_host, port=redis_port),
    )
    
if __name__ == "__main__":
    # 配置文件基础
    cp = ConfigParser(config_file="base.cfg")
    config_dict = get_config()

    # 填写配置文件
    for k in config_dict.keys():
        cp.add_section(k)
        for k_inner in config_dict[k]:
            cp.set_kv(k_inner, config_dict[k][k_inner])