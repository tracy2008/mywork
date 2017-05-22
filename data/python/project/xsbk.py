# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

class QSBK:
	def _init_(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = {'User-Agent':self.user_agent}
		self.stories = []
		self.enable = False
	def getPage(self, pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print e.reason
				return None
	def getPageItems(self,pageIndex):
		print "getPageItems..."
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print "error..."
			return None
		pattern = re.compile('<div.*?author.*?">.*?<a.*?<img.*?<a.*?<h2>(.*?)</h2>.*?<div.*?>(.*?)</div>.*?<div.*?'+
                         'content">.*?<span>(.*?)</span>.*?<img.*?<div class="stats.*?class="number">(.*?)</i>',re.S)
		items = re.findall(pattern,pageCode)
		pageStories = []
		for item in items:
			replaceBR = re.compile('<br/>')
			text = re.sub(replaceBR,"\n",item[2])
			pageStories.append([item[0].strip(),text.strip()])
		return pageStories
	def loadPage(self):
		print "loadPage..."
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				print pageStories
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	def getOneStory(self,pageStories,page):
		print "getOneStory..."
		for story in pageStories:
			self.loadPage()
			print u"第%d页\t发布人:%s\n%s" %(page,story[0],story[1])

	def start(self):
		self._init_()
		# print u"正在读取嗅事百科，按回车查看新段子，Q退出"
		self.enable = True

		self.loadPage()
		nowPage = 0
		# print self.enable
		if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)
		# while self.enable:
		# 	if len(self.stories) > 0:
		# 		pageStories = self.stories[0]
		# 		nowPage += 1
		# 		del self.stories[0]
		# 		self.getOneStory(pageStories,nowPage)
spider = QSBK()
spider.start()
