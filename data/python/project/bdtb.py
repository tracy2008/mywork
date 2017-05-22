# coding=UTF-8
import urllib
import urllib2
import re
import tool
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
class BDTB:
	def __init__(self,baseUrl,seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = tool.Tool()
		self.file = None
		self.floor = 1
		self.defaultTitle = '百度贴吧'
	def getPage(self,pageNo):
		try:
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNo)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			return response.read()
		except urllib2.URLError,e:
			if hasattr(e,"reason"):
				print e.reason
				return None
	#获取帖子标题
	def getTitle(self, page):
		regrex = '<h3 class="core_title_txt.*?>(.*?)</h3>'
		pattern = re.compile(regrex,re.S)
		result = re.search(pattern,page)
		if result:
			# print result.group(1)
			return result.group(1).strip()
		else:
			return None
	#获取帖子一共多少页
	def getPageTotal(self,page):
		regrex = '<li class="l_reply_num.*?<span.*?<span.*?>(.*?)</span>'
		pattern = re.compile(regrex,re.S)
		result = re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None
	#提取正文内容
	def getContent(self, page):
		regrex = '<div id="post_content_.*?>(.*?)</div>'
		pattern = re.compile(regrex,re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			content = '\n' + self.tool.replace(item) + '\n'
			contents.append(content.encode('utf-8'))
		return contents
	def setFileTitle(self, title):
		if title is not None:
			self.file = open(title + ".txt", "w+")
		else:
			self.file = open(self.defaultTitle + ".txt", "w+")
	def writeData(self, contents):
		for item in contents:
			floorLine = "\n" + str(self.floor) + "楼---------------------------------\n"
			self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1
	def start(self):
		indexPage = self.getPage(1)
		pageTotal = self.getPageTotal(indexPage)
		title = self.getTitle(indexPage)
		self.setFileTitle(title.decode('utf-8'))
		try:
			print '共有'+ pageTotal + '页'
			for i in range(1,int(pageTotal) + 1):
				page = self.getPage(i)
				contents = self.getContent(page)
				self.writeData(contents)
		except IOError,e:
			print e.message
		finally:
			print 'finished'
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.start()
