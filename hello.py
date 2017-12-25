#encoding:utf8
import tornado.web
import tornado.ioloop

class Index_handler(tornado.web.RequestHandler):
	def get(self):

		self.write('孬')

if __name__=='__main__':

	app = tornado.web.Application([(r'/',Index_handler)])
	app.listen(8001)
	tornado.ioloop.IOLoop.current().start()