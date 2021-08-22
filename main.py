# -*- coding: utf-8 -*-
# @Time : 2021/8/22 12:12
# @Author : lemon
# @File : main.py
# @Software: PyCharm

import sys
from scrapy.cmdline import execute
import os

if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # TODO 填充spider名称
    execute(['scrapy', 'crawl', 'spider_name'])