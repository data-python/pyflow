#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /PyWebView/vue-pywebview-pyinstaller/pyapp/api/api.py
Author: 潘高
LastEditors: 潘高
Date: 2022-03-21 17:01:39
LastEditTime: 2022-03-23 15:40:25
Description: 本地API，供前端JS调用
usage: 调用window.pywebview.api.<methodname>(<parameters>)从Javascript执行
'''

import getpass
import os
import webview
from decimal import Decimal

from utils.pdf_outline_utils import gen_pdf_outlines
from utils.remove_bg_utils import remove_bg
from utils.convert_json_to_csv_utils import convert_json_to_csv
from utils.extract_urls_utils import extract_url
from utils.deploy_fe_project_utils import deploy_fe_project
from utils.handright_utils import get_handwrite
from utils.extract_news_utils import extract_news, extract_html
from utils.tinydb_utils import *

class API:

    def getOwner(self):
        return getpass.getuser()

    def getSum(self, a, b):
        # print(str(a), str(b))
        return str(Decimal(str(a)) + Decimal(str(b)))

    def readContent(self, filePath):
        file_object = open(filePath, encoding='utf-8')
        all_the_text = ""
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        return all_the_text
      
    # 执行字符串  
    def execCodeStr(self, str):
        exec(str)
        return '代码执行成功'

    def execPyFile(self, pyFilePath, *argv):
        print(argv)
        argvStr = ''
        for arg in argv:
             argvStr = argvStr + ' "' + arg + '"'
        
        cmd = 'python ' + pyFilePath + argvStr
        print(cmd)
        return True if os.system(cmd) == 0 else False

    def makeDir(self, dir):
        os.makedirs(dir)
        return dir
    
    def writeFile(self, filePath, content):
        file = open(filePath, mode='w', encoding="utf-8")
        return file.write(content)

    def openFiles(self):
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True)
        return result

    def openPicFile(self):
        file_types = ('Image Files (*.png;*.jpg)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        return result

    def openJsonFile(self):
        file_types = ('Json Files (*.json)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        return result

    def openPdfFile(self):
        file_types = ('Pdf files (*.pdf)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        return result

    def openPyFile(self):
        file_types = ('Python files (*.py)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        return result

    def openFontFile(self):
        file_types = ('font files (*.ttf)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        return result

    def openFolder(self):
        result = self.window.create_file_dialog(webview.FOLDER_DIALOG)
        return result

    def genPdfOutlines(self, pdfPath):
        return gen_pdf_outlines(pdfPath)

    def removeBg(self, picPath, apiKey):
        return remove_bg(picPath, apiKey)

    def json2csv(self, jsonPath):
        return convert_json_to_csv(jsonPath)

    def extractUrl(self, url):
        return extract_url(url)

    def deployFe(self, project_path, remote_path, hostname, username, password, buildCmd, distPath):
        return deploy_fe_project(project_path, remote_path, hostname, username, password, buildCmd, distPath)

    def handwrite(self, text, fontPath, outPath):
        return get_handwrite(text, fontPath, outPath)
    
    def extractNews(self, url):
        return extract_news(url)
    
    def extractHTML(self, html):
        return extract_html(html)
    
    # 查询全部
    def listTable(self, table_name):
        return list_table(table_name)

    # 获取第一个元素
    def getTable(self, table_name):
        return get_table(table_name)

    # 获取第一个元素
    def getTableFirst(self, table_name):
        return get_table_first(table_name)
    
    # 获取最后一个元素
    def getTableLast(self, table_name):
        return get_table_last(table_name)

    # 按键值查询
    def getTableByCondition(self, table_name, key, value):
        return get_table_by_condition(table_name, key, value)

    # 插入一条数据
    def insertTable(self, table_name, data):
        return insert_table(table_name, data)


    # 插入多条数据
    def insertTableMul(self, table_name, array):
        return insert_table_multiple(table_name, array)

    # 按键值更新
    def updateTableByCondition(self, table_name, data, key, value):
        return update_table_by_condition(table_name, data, key, value)

    # 按ID插入或更新
    def upsertTable(self, table_name, data, id):
        return upsert_table(table_name, data, id)

    # 按键值插入或更新
    def upsertTableByCondition(self, table_name, data, key, value):
        return upsert_table_by_condition(table_name, data, key, value)

    # 删除表格
    def deleteTable(self, table_name):
        return elete_table(table_name)

    # 按ID删除
    def removeTable(self, table_name, id):
        return remove_table(table_name, id)

    # 按照键值删除
    def removeTableByCondition(self, table_name, key, value):
        return remove_table_by_condition(table_name, key, value)

    # 按IDs批量删除
    def removeTableBatch(self, table_name, ids):
        return remove_table_batch(table_name, ids)

    