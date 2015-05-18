import random

class ProxyMiddleware(object):
	def process_request(self, request, spider):
		#request.meta['proxy'] = "http://219.159.199.6:9999"
		ProxyServer = [
						"http://111.1.23.197:80",
						"http://115.238.226.185:80",
						"http://115.238.226.168:80",
						"http://122.226.183.148:80",
						"http://125.39.17.117:80",
		]
		index = random.randint(2, 4) 
		request.meta['proxy'] = ProxyServer[index]

