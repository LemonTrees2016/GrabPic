#!/usr/bin/python

import urllib
import urllib2
import re

URL="http://tieba.baidu.com/p/2460150866"
URL1="http://desk.zol.com.cn/"
def getHtml(url):
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	try:
		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		html = response.read()
		return html
	except urllib2.URLError, e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason

def getImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1

html = getHtml(URL1)

print getImg(html)

