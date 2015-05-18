import scrapy
import re
import json
from scrapy import Selector
from scrapy.http import FormRequest
from scrapy.http import Request

global xsrf
xsrf = ''

class zhihu(scrapy.Spider):
	name = "Zhihu"
	start_urls = ["http://www.zhihu.com"]
	headers = {'ccept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
	           'Accept-Encoding':'gzip,deflate,sdch',
	           'Accept-Language':'zh-CN,zh;q=0.8',
	           'Cache-Control':'max-age=0',
	           'Connection':'keep-alive',
	}

	def start_requests(self):
		return [Request("http://www.zhihu.com/login", meta = {'cookiejar' : 1}, 
				headers = self.headers, 
				callback = self.post_login)]

	def post_login(self, response):
		global xsrf
		xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
		return [FormRequest.from_response(response,
				meta = {'cookiejar':response.meta['cookiejar']},
				formdata = {
				'_xsrf': xsrf,
				'email': 'YOUR_EMAIL',
				'password': 'YOUR_PASSWORD'
				},
				callback = self.preparse,
				dont_filter = True
				)]

	def preparse(self, response):
		global xsrf
		xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
		return [FormRequest("http://www.zhihu.com/log/questions",
				meta = {'cookiejar':response.meta['cookiejar']},
				formdata = {
				'start': '932761103',
				'offset': '0',
				'_xsrf': xsrf
				},
				callback = self.parse,
				dont_filter = True
				)]

	def parse(self, response):
		global xsrf
		j = json.loads(response.body)
		page = j['msg'][1]
		urls = re.findall(r"/question/\d{8}", page)
		items = re.findall(r"logitem-\d{9}", page)
		lastitems = items[len(items) - 1][8:]
		if urls and items:
			for i in range(0, len(urls) - 1):
				print urls[i] + "--->" + items[i] 

		return [FormRequest("http://www.zhihu.com/log/questions",
				meta = {'cookiejar':response.meta['cookiejar']},
				formdata = {
				'start': lastitems,
				'offset': '0',
				'_xsrf': xsrf
				},
				dont_filter = True
				)]

