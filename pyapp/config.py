#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /PyWebView/vue-pywebview-pyinstaller/pyapp/config/config.py
Author: 潘高
LastEditors: 潘高
Date: 2022-03-21 16:54:23
LastEditTime: 2022-03-23 15:40:01
Description: 配置文件
usage: 
    from pyapp.config import Config
    cfg = Config()
'''

import platform
import time

appVersion = "20220622"

class Config:    
    appName = 'pyflow-' + appVersion # 应用名称
    appVersion = appVersion  # 应用版本号
    appSystem = platform.system()    # 本机系统类型
