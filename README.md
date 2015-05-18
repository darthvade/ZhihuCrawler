###Zhihu Crawler
================

####Overview
	The goal of this project is helping geeks to get Zhihu.com's Questions easily.
	Up to Now, this project includes only one module(or you can say a spider) 
	called ZhihuSpiderQuestionID.
================

####Requirements(developed with)
	Ubuntu 14.04 LTS
	Python 2.7.6
	Scrapy 0.24.6
================

####How to use
#####Module1(ZhihuSpiderQuestionsID)
	1. git clone https://github.com/darthvade/ZhihuCrawler.git
	2. cd ZhihuCrawler/ZhihuSpiderQuestionsID
	3. scrapy crawl Zhihu
#####Module2(ZhihuSpiderQuestionsInfos)
	TODO
================

####Notes of Modules
#####Module1(ZhihuSpiderQuestionsID)
	The purpose of this module is to download Zhihu questions' IDs as much 
	as possible.
	If you have own the ID of a question, you can easily constract a usable 
	URL of this question under Zhihu.com.

	eg. ID is 30462127, then URL is http://www.zhihu.com/question/30462127
	
	So, this Module do some preparations for the following modules to 
	crawl all the content of questions.
