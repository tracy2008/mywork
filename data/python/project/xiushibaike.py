import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.15'
headers = {'User-Agent':user_agent}
try:
	request = urllib2.Request(url,headers=headers)
	response = urllib2.urlopen(request)
	# print response.read()
	content = response.read().decode('utf-8')
	pattern = re.compile('<div.*?author.*?">.*?<a.*?<img.*?<a.*?<h2>(.*?)</h2>.*?<div.*?>(.*?)</div>.*?<div.*?'+
                         'content">.*?<span>(.*?)</span>.*?<img.*?<div class="stats.*?class="number">(.*?)</i>',re.S)
	items = re.findall(pattern,content)
	for item in items:
		print item[0]
		print item[1]
		print item[2]
		print item[3]
		print '========================'
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
