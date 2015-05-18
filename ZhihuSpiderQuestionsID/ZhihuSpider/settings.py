# -*- coding: utf-8 -*-

# Scrapy settings for ZhihuSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ZhihuSpider'

SPIDER_MODULES = ['ZhihuSpider.spiders']
NEWSPIDER_MODULE = 'ZhihuSpider.spiders'

#Because of some unclear reason, this Proxy is NOT supported

#DOWNLOADER_MIDDLEWARES = {
#	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':110,
#	'ZhihuSpider.ProxyMiddlewares.ProxyMiddleware':100,
#}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ZhihuSpider (+http://www.yourdomain.com)'
