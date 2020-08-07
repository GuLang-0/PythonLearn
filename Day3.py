#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Learning Diary'

__author__ = 'GuLang0'

#---2020-08-06---
#Module(模块)
#模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，
#检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。

#运行测试：
#if __name__=='__main__':
#       test()

#private函数和变量      _xxx  __xxx


#OOP
#类名通常是大写字母开头的单词
class Student(object):
    def __init__(self, name):
        self.name = name
