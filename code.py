#!/usr/bin/env python
# coding: utf-8

import sys
import web
from config import url

# 将 controllers 目录加入到当前环境变量中，这样的好处是方便写 url 时不多写这么多字符串。
sys.path.append('./controllers')
urls = url.urls

if __name__ == "__main__":
    app = web.application(urls, globals(),autoreload=True)
    app.run()
