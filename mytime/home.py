"""
尝试在本地直接部署服务 flask - nginx - tornado
已修改Nginx 配置文件， 但是本地使用的小米路由器无线网，输入网址或ip会直接转入小米路由器管理页面

"""

import sys
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from main import app

if len(sys.argv) == 2:
    port = sys.argv[1]
else:
    port = 5000

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port)
print("success")
IOLoop.instance().start()
