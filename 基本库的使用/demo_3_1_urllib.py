"""
urllib 基本库的使用
Author: lq0916
24 7 26
"""
"""
Title:Urllib库的基本使用
Author:无医
Time:2024/7/26 
"""


### 初级使用 get
# urlopen的基本使用
import urllib.request


def fun_urlopen():
	import urllib.request
	response = urllib.request.urlopen("https://www.python.org")
	print(response.status)
	print(response.getheaders())
	print(response.getheader('Server'))
# fun_urlopen()

# urlopen函数的api
# url,data=None,[timeout,]*,cafile=None,cadefault=False,context=None

# data 参数 ->若传递了则为post请求方式
def fun_urlopen_data():
	import urllib.parse
	import urllib.request

	data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
	response = urllib.request.urlopen('http://httpbin.org/post',data=data)
	# bytes()转字节流 第一个参数是str类型  第二个参数指定编码方式
	# urllib.parser.urlencode()将参数字典转换为字符串
	print(response.read())
# fun_urlopen_data()

# timeout 参数 ->若请求超出了设置的时间没有响应则抛出异常
def fun_urlopen_timeout():
	import urllib.request

	response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
	print(response.read())
def fun_urlopen_timeout1():
	import socket
	import urllib.request
	import urllib.error
	try:
		response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
	except urllib.error.URLError as e:
		if isinstance(e.reason,socket.timeout):
			print('TIME OUT')
# fun_urlopen_timeout1()

###### 中级使用 post
# request的使用
def fun_request():
	import urllib.request

	request = urllib.request.Request('http://python.org')
	response = urllib.request.urlopen(request)
	print(response.read().decode('utf-8','ignore'))
#fun_request()

# class urllib.request.Request ( url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None) 
# url 必传 其余皆非 data为字节流类型 若字典可用urllib.parser.urlencode()
# headers  请求头 字典  可以通过参数构造或者调用请求实例add_header()添加   
# origin_req_host  请求方的ip地址或者host名字
# unverifiable 请求是否无法验证
# method 指示请求的方法
def fun_request_post1():
	from urllib import request, parse
	url = 'http://httpbin.org/post'
	headers = {
	'User-Agent':'Mozilla/4.0(compatible; MSIE 5.5;Windows NT)',
	'Host':'htppbin.org'
	}
	dict = {
	'name':'Germey'
	}
	data = bytes(parse.urlencode(dict),encoding='utf8')
	req = request.Request(url=url,data=data,headers=headers,method='POST')
	response = request.urlopen(req)
	print(response.read().decode('GBK'))

def fun_request_post2():
	from urllib import request, parse
	url = 'http://httpbin.org/post'
	dict = {
	'name':'Germey'
	}
	data = bytes(parse.urlencode(dict),encoding='utf8')
	req = request.Request(url=url,data=data,method='POST')
	req.add_header('User-Agent','Mozilla/4.0(compatible;MSIE 5.5;Windows NT)')
	response = request.urlopen(req)
	print(response.read().decode('GBK'))
# fun_request_post2()

##### 高级使用
# 处理cookies 代理设置
#Handler的使用

# 密码验证
def fun_HTTPpBasicAuthHand():
	from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
	from urllib.error import URLError

	username = 'username'
	password = 'password'
	url = 'http://localhost:5000/'

	p = HTTPPasswordMgrWithDefaultRealm()
	p.add_password(None,url,username,password)
	auth_handler = HTTPBasicAuthHandler(p)
	opener = build_opener(auth_handler)

	try:
		result = opener.open(url)
		html = result.read().decode('utf-8')
		print(html)
	except URLError as e:
		print(e.reason)

# fun_HTTPpBasicAuthHand()

# 代理
def fun_url_daili():
	from urllib.error import URLError
	from urllib.request import ProxyHandler,build_opener
	proxy_handler = ProxyHandler({
		'http':'http://127.0.0.1:8080',
		'https':'https://127.0.0.1:8080'
		})
	opener = build_opener(proxy_handler)
	try:
		response = opener.open('https://www.baidu.com')
		print(response.read().decode('utf-8'))
	except URLError as e:
		print("错误原因：",e.reason)
#fun_url_daili()

# cookies 处理

# 获取cookies
def fun_url_cookies():
	import http.cookiejar,urllib.request

	cookie = http.cookiejar.CookieJar()
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open('http://www.baidu.com')
	for item in cookie:
		print(item.name+"="+item.value)
# fun_url_cookies()

def fun_url_cookies_to_text():
	# 获取网站的cookies
	import http.cookiejar, urllib.request

	filename = 'cookie_Mo.txt'
	# 生成文件时候的用到  是CookiesJar的子类 用于处理cookies和文件相关的时间  读取或保存
	cookie = http.cookiejar.MozillaCookieJar(filename)
	handler = urllib.request.HTTPCookieProcessor(cookie)
	# 使用build_opener 构建出opener 执行open()函数
	opener = urllib.request.build_opener(handler)
	response = opener.open('http://www.baidu.com')
	cookie.save(ignore_discard=True,ignore_expires=True)
fun_url_cookies_to_text()

def fun_url_cookies_to_text_LWP():
	# 获取网站的cookies
	import http.cookiejar, urllib.request

	filename = 'cookie_LWP.txt'
	# 生成文件时候的用到  是CookiesJar的子类 用于处理cookies和文件相关的时间  读取或保存
	# 此外 LWPCookiesJar同作用  保存格式不同  为LWP
	cookie = http.cookiejar.LWPCookieJar(filename)
	handler = urllib.request.HTTPCookieProcessor(cookie)
	# 使用build_opener 构建出opener 执行open()函数
	opener = urllib.request.build_opener(handler)
	response = opener.open('http://www.baidu.com')
	cookie.save(ignore_discard=True,ignore_expires=True)
# fun_url_cookies_to_text_LWP()

# 如何使用获取的cookies
# 根据LWPCookieJar格式
def fun_url_use_cookie():
	import http,urllib

	cookie = http.cookiejar.LWPCookieJar()
	# 导入cookies文件
	cookie.load('cookie_LWP.txt', ignore_discard=True, ignore_expires=True)
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open('http://www.baidu.com')
	print(response.read().decode('utf-8'))

fun_url_use_cookie()
