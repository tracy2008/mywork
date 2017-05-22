import urllib2
# response = urllib2.urlopen("http://www.qiushibaike.com/hot/page/1")
response = urllib2.urlopen("http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1")
print response.read()