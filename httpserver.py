#encoding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver


class Index_handler(tornado.web.RequestHandler):
	def get(self):
		self.write("<h1><a href='#'>这个是httpserver的写法</a></h1>")


if __name__=='__main__':
	app = tornado.web.Application([(r'/',Index_handler)])
	http_server= tornado.httpserver.HTTPServer(app)
	http_server.listen('8002')
	tornado.ioloop.IOLoop.current().start()