import tornado.ioloop
import tornado.web
from BeautifulSoup import BeautifulSoup
import os

# print 
class MainRequestHandler(tornado.web.RequestHandler):
	def get(self):
		page = self.request.uri.replace("/","")
		filen = page
		if len(page) == 0 or page == 'home':
			page = "home"
			filen = "home"
		navbar = BeautifulSoup(open("navbar").read())
		content = open(page + ".html").read()
		navbar.findAll('a', href=filen)[0].parent['class'] = 'active'
		#change here
		shell = "<html><head><title>DISCIce-AQ: " + page + "</title><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><!-- Bootstrap --><link href=\"static/css/bootstrap.min.css\" rel=\"stylesheet\" media=\"screen\"></head><body>"
		sidebar = open("sidebar").read()
		fullbody = str(navbar) + sidebar + str(content)
		fullpage = shell + fullbody + "</div></div></body></html>"
		self.write(fullpage)

settings = {"static_path": os.path.dirname(os.path.realpath(__file__)) + "/static"}
handlers = [(r".*", MainRequestHandler)]

app = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
	app.listen(80)
	tornado.ioloop.IOLoop.instance().start()
