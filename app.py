import cherrypy
import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))

class RootPage:

	def index(self):
		raise cherrypy.HTTPRedirect("/static/index.html")

	def getMachineInfo(self):
		return "hello"

	index.exposed = True
	getMachineInfo.exposed = True

if __name__ == '__main__':
	conf = {
				'global': {
					'server.socket_host': '0.0.0.0',
					'server.socket_port': 80,
					'server.threaed_pool': 50
				},

				'/': {
					'tools.staticdir.root': current_dir
				},

				'/static': {
					'tools.staticdir.on': True,
					'tools.staticdir.dir': 'static'
				}

			}
	cherrypy.quickstart(RootPage(), config=conf)
