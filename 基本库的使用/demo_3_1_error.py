"""
Title:异常处理和链接解析
Author:无医
Time:2024/7/28
"""


# -------处理异常------------
# URLErroe

# urllib 中 error 模块
# URLError 来自于 urllib中的error模块 继承OSError，由request 产生的异常都可捕获
def fun_URLError_test():
    from urllib import request, error

    try:
        response = request.urlopen('http://cuiqingcai.com/index.htm')
    except error.URLError as e:
        print(e.reason)
# fun_URLError_test()

# HTTPError
# URLError 的子类  处理 HTTP请求错误  例如 认证请求失败
# code 返回状态码
# reason 同父类  返回错误原因
# headers 返回请求头
def fun_HTTPError_test():
    from urllib import request, error

    try:
        response = request.urlopen('http://cuiqingcai.com/index.htm')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers,sep='\n')
# fun_HTTPError_test()

# error 中 http是url子类  可以先选择捕获子类错误 再捕获父类错误

def fun_HTTPError_1():
    from urllib import request,error

    try:
        response = request.urlopen('http://cuiqingcai/index.htm')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print("Response succfully")
# fun_HTTPError_1()

# sometime reason type return is object ,not is str
# 此例子中直接设置超时时间来抛出 timeout异常
def fun_Error_reason_Test():
    import socket
    import urllib.request
    import urllib.error

    try:
        response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')
# reason 属性为socket.timeout 类
# fun_Error_reason_Test()

# -------解析链接------------
# urllib库中提供了parse模块  定义url的标准接口
# 例如实现url 各部分的抽取 合并 链接转换
#
# 1.urlparse()
#   ->urlparse(url, scheme='', allow_fragments=True):
#   ->实现url的识别和分段
#   ->返回ParseResult类型对象: scheme  netloc path params query fragment
#   ->scheme://netloc/path;params?query#fragment
def fun_urlparse_test():
    from urllib.parse import urlparse

    result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    print(type(result), result, sep='\n')
    print("实际返回为元组")
    print("由索引顺序,或者属性名")
    print(result[0],result.scheme,result[1],result.netloc,sep='\n')
# fun_urlparse_test()

def fun_urlparse_test_2():
    from urllib.parse import urlparse

    result_1 = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    result_2 = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='http')
    result_3 = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)

    print("allow_fragments  = False", result_1)
    print("无scheme:",result_2)
    print("无params和query:",result_3)
# fun_urlparse_test_2()

# 2.urlunparse()
# urlparse()的对立方法   接受参数是一个可迭代的对象 长度为6 否则 抛出异常
def fun_urlunparse_test():
    from urllib.parse import urlunparse

    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urlunparse(data))
# fun_urlunparse_test()

# 3.urlsplit()
# 与urlparse相似 不单独解析params 返回五个结果 将params 合并的path中
# 同理亦可 根据索引或属性名
def fun_urlsplit_test():
    from urllib.parse import urlsplit

    result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
    print(len(result),result,sep='\n')
    print("由索引顺序,或者属性名")
    print(result[0],result.scheme,result[1],result.netloc,sep='\n')
# fun_urlsplit_test()

# 4.urlunsplit()
# 与urlunparse()相似 不赘述
def fun_urlunsplit_test():
    from urllib.parse import urlunsplit

    data = ['http', 'www.baidu.com', 'index.html','a=6', 'comment']
    print(urlunsplit(data))
# fun_urlunsplit_test()

# 5.urljoin()
# 有了urlunparse 和 urlunsplit 则可根据定长对象完成合并
# urljoin 采用 base_url作为第一参数 将新的链接作为第二个参数  方法会分析base_url的scheme  netloc path 对新链接缺失的内容进行补充
def fun_urljoin_test():
    from urllib.parse import urljoin

    print(urljoin('http://www.baidu', 'FAQ.hitml'))
    print(urljoin('http://www.baidu', 'http://www.cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu/about.html', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu/about.html','http://www.cuiqingcai.com/FAQ.html?qestion=2'))
    print(urljoin('http://www.baidu.com','?category=2#comment'))
    print(urljoin('www.baidu.com#comment','?category=2'))
# fun_urljoin_test()

# 6.urlencode()
# 用于构造get请求参数
# 使用字典将参数表示出来  之后调用方法 将其序列化为get请求参数

def fun_urlencode_test():
    from urllib.parse import urlencode

    params = {
        'name': 'germey',
        'age': 22
    }
    base_url = 'http://www.baidu.com'
    url = base_url + urlencode(params)
    print(url)
# fun_urlencode_test()

# 7.parse_qs
# 反序列化 <-> urlencode
# 将get请求转为字典
def fun_parse_qs_test():
    from urllib.parse import parse_qs

    query = 'name=germey&age=22'
    print(parse_qs(query))
# fun_parse_qs_test()

# 8.parse_qsl()
# 将参数转化为元组组成的列表
def fun_parse_qsl_test():
    from urllib.parse import parse_qsl
    query = 'name=germey&age=22'
    print(parse_qsl(query))
    # [('name', 'germey'), ('age', '22')]
# fun_parse_qsl_test()

# 9.quote()
# 将内容转换为url编码格式 url带有中文参数的时候可能会导致乱码问题 此时可用此方法
def fun_quote_test():
    from urllib.parse import quote

    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd='+ quote(keyword)
    print(url)
# fun_quote_test()

# 10.unquote
# 将url进行解码
def fun_unquote_test():
    from urllib.parse import unquote

    url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    print(unquote(url))
# fun_unquote_test()

# 分析Robots协议 ->urllib.robotparser模块
# robots.txt 爬虫协议 网络爬虫排除标准
# 我反正不看 哈哈哈
# 爬虫名称

# robotparser
# 使用该模块解析robots.txt ->RobotFileParser

def fun_robotparser_test():
    from urllib.robotparser import RobotFileParser

    rp = RobotFileParser() # rp = RobotFileParser('http://www.jianshu.com./robots.txt')
    rp.set_url('http://www.jianshu.com./robots.txt')
    rp.read()
    print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
# fun_robotparser_test()
def fun_robotparser_test_parser():
    from urllib.robotparser import RobotFileParser
    from urllib.request import urlopen

    rp = RobotFileParser()
    rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
fun_robotparser_test_parser()













