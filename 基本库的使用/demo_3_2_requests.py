"""
Title:Request库的基本使用
Author:无医
Time:2024/7/28 
"""


# 基本使用  安装 pip install request
# urllib 中urlopen 以Get方式请求网页  ->request get方法
# 获取的为Response对象
def fun_request_test():
    import requests

    r = requests.get('http://wwww.baidu.com/')
    print(type(r))  # Response对象
    print(r.status_code)  # 状态码
    print(type(r.text))  # 响应体的类型
    print(r.text)  # 响应体的内容
    print(r.cookies)  # Cookies

    # 方便于其他请求类型依然可以使用一句话完成
    r = requests.post('http://httpbin.org/post')
    r = requests.put('http://httpbin.org/put')
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')


# fun_request_test()

# GET 请求
# get->简单的实例  网站判断为get请求返回对应的请求信息
def fun_Get_test():
    import requests

    r = requests.get('http://httpbin.org/get')
    # 返回结果包括请求头 URL IP等
    print(r.text)


# fun_Get_test()

# get->附加参数 使用 params参数
def fun_Get_test_add_():
    import requests

    data = {
        "name": "germey",
        "age": "22"
    }
    r = requests.get("http://httpbin.org/get", params=data)
    # r = requests.get("http://httpbin.org/get?age=22&name=germey")
    print(type(r.text))
    print(r.text)
    # 返回类型是一个str ->json格式 可以调用json()转变为字典
    # 如果返回结果不是json格式则会抛出异常
    print('json->字典')
    print(r.json())
    print(type(r.json()))


# fun_Get_test_add_()

# 抓取网页
def fun_request_scrap_test():
    import requests
    import re

    # r = requests.get("https://www.zhihu.com/explore")
    # print(r.text)
    # 如果不添加headers 可能无法请求

    # 添加headers ->参数中可以任意添加字段
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get("https://www.zhihu.com/explore", headers=headers)
    print(r.text)
    # 正则表达式
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)  # 已经失效需要重新考虑
    titles = re.findall(pattern, r.text)
    print(titles)


# fun_request_scrap_test()

# 抓取二进制数据
# 上面的案例返回一个html文档

# 抓取github的站点图标
def fun_Scrap_Github_ico_Test():
    import requests

    r = requests.get("https://github.com/favicon.ico")
    # 返回的是Response对象  两个属性 text  content
    print(type(r))
    print(r.text)  # 乱码 由于图片是二进制数据  打印为str  则乱码
    print(r.content)  # 结果前面带有b -> bytes类型数据
    # 保存图片 ->音频和视频同理
    with open('github_favicon.ico', 'wb') as f:
        f.write(r.content)


# fun_Scrap_Github_ico_Test()

# post请求
def fun_post_test():
    import requests
    data = {'name': 'germey', 'age': '22'}
    r = requests.post("http://httpbin.org/post", data=data)
    print(r.text)  # 返回结果中form部分为提交的数据


# fun_post_test()

# 响应
# 发送请求之后获得响应  再上面的实例中我们使用了text和content
# 此外还有很多的属性方法 requests.Response

def fun_requests_get_test():
    import requests

    r = requests.get("http://www.jianshu.com")
    print(type(r.status_code), r.status_code)  # 状态码
    # requests内置状态码查询对象requests.codes
    exit() if not r.status_code == requests.codes.ok else print("Requests Successful!")

    print(type(r.headers), r.headers)  # 响应头
    print(type(r.cookies), r.cookies)  # Cookies
    print(type(r.url), r.url)  # url
    print(type(r.history), r.history)  # 请求历史


# fun_requests_get_test()

# 高级用法

# 文件上传
def fun_file_post_test():
    import requests

    files = {'file': open('github_favicon.ico', 'rb')}
    r = requests.post("http://httpbin.org/post", files=files)
    print(r.text)
    # 响应头中会包含files这个字段  form字段是空的


# fun_file_post_test()
# Cookies->获取cookies
def fun_requests_cookies_test():
    import requests

    r = requests.get("http://www.baidu.com")
    print(r.cookies)  # Cookies为RequestsCookieJar类
    for key, value in r.cookies.items():
        print(key + '=' + value)


# fun_requests_cookies_test()

# 使用cookies
def fun_requests_use_cookies_test():
    import requests
    # headers = {
    #     'Cookies': '_xsrf=3Clan9uqt4VhubG8cEfa9mKoXNN8F0F4; _zap=754fb133-f571-42e2-9eb0-6588353a49b0; d_c0=AEASqWdG5BiPTp3f3lPjIwOs__UveV1Zd7c=|1720416137; __snaker__id=6NG0szpTYMcCHkF6; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1720416138,1722238583; HMACCOUNT=53125E72EC626B42; captcha_session_v2=2|1:0|10:1722262386|18:captcha_session_v2|88:SEJxZGV4TUJ2ejZVS2ZiOXZScWFUQjg3R2ljR05ldVBVRkRUbFQzb0xZLzBNVkhWU2VkL2Z0bGZZT0s1Q2h6NA==|b6bd470987398efe10d140414113720297f8e42cf4f337b67f8abcfc0039775f; SESSIONID=JfWFnK9cwkAy6djCeToAo1wTbiYoTLJZcu28kWw9iSC; JOID=UVkTAEi_oaGaqfNdAb6zNpXEtbsc98Dz3Me6Y2fIyOfmn5c1RcgAA_yr9l8E0oKYrEj0esV5zzSnEPsd91JXqm8=; osd=VF0cB0u6pa6dqvZZDrmwM5HLsrgZ88_038K-bGDLzePpmJQwQccHAPmv-VgH14aXq0vxfsp-zDGjH_we8lZYrWw=; gdxidpyhxdE=%5CNxE9WjII1lsJS%2FdA8sME%2BocVe5UourlOhk0krkAoN%2FXtZeT3IyYO3%2BwjHxN%5CYocnbXxMYXpw3LsG9BDtG7dTthNLQp0ar%5C1c3athak2xIOoC3ZZpkyYLspNrJ%2BYUSskH%2BlOev8vchDIAaRJh%5Ci1p%5C0ctTc9HXukuj8CPYjS1kIpEOaw%3A1722263287443; captcha_ticket_v2=2|1:0|10:1722262401|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfRUNUZU82TUVvYlV4V1lzd09yMHluRDRuZ1Z1QUNYTVlKbk1WWlMzbFpxdXpLeW5DMkRSVWVyNHZSdSpSc3FYTmpFVFJDWGlFTklvU3pfZDNxV0taU3lhQVFrRFR2bVZlLktWOWRJa3ExaVNBbmxIZFFYbjN4Z0M4Ujg0OGtBbU9RVDR0dE9XSHZzbnBfaFVxT3pob3QyRlhzQmdEemY1VnBseDk5WUdzYmUzLkl2TEFhQ3IuY2xoOFRrRjU0Z0lVRkFUSEd5b3lQS29XNkxKeXhPQmtKeXFOZnVTRkFVT29rSFRpbnZpNlg2QWZUcG5wVmJ5LlJjR2x6MW4ydWp0bi5TblFNaGVjbjRTV0cudkVQc2NMd05QdWd3ZXNCQjZiUExBSGNTM3NWZ3J3Ujh4VFNiLmFRampCViozTTkxbmd0VV9udWoxayplcWpDVVdxNlBtczVaVEsqR3NGNERVV3FDajQzV2t5bGFXR2pYZU14Zzg0eC5DQUlYTW00bG1EbkJnYVpRRmZqUHJBelhfMFpwREFrUFBuaGpVVGF5V0t1eUtTdXlyZUdreUJtOW1KTWFGVzlOb1pEOW1GZzU2cXZSTEhDdWtGdUdHVEZ6emk1QjVGUjVrb3lSOFAybWwzX042QWs2OENVUEFRTVBVcEtzQUlmMWtqTDhHcnQ5aC42V2hYQVg3N192X2lfMSJ9|0bc4eb5e6aeebfc713221f537c3fd5d9716611a117630ca267c77d0db6b208d4; z_c0=2|1:0|10:1722262418|4:z_c0|92:Mi4xczFPZ0lRQUFBQUFBUUJLcFowYmtHQ1lBQUFCZ0FsVk5rdkdVWndDdThveGstSWpqa0RNeXFZTEtQZDVxXy1HdXR3|a868cfc71c9e673bf3d9d72c03884e6da936a44a9bad508fb8a94284022ecbe7; q_c1=d77241c4f26d4bddae07d6ce05167b08|1722262419000|1722262419000; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1722262420; tst=r; BEC=244e292b1eefcef20c9b81b1d9777823',
    #     'Host': 'www.zhihu.com',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    # }
    # r = requests.get('http://www.zhihu.com', headers=headers)
    # with open('zhihu_test.html', 'wb') as f:
    #     f.write(r.content)
    # 也可以通过cookies参数来设置 ->需要构建RequestCookiesJar对象
    cookies = '_xsrf=3Clan9uqt4VhubG8cEfa9mKoXNN8F0F4; _zap=754fb133-f571-42e2-9eb0-6588353a49b0; d_c0=AEASqWdG5BiPTp3f3lPjIwOs__UveV1Zd7c=|1720416137; __snaker__id=6NG0szpTYMcCHkF6; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1720416138,1722238583; HMACCOUNT=53125E72EC626B42; captcha_session_v2=2|1:0|10:1722262386|18:captcha_session_v2|88:SEJxZGV4TUJ2ejZVS2ZiOXZScWFUQjg3R2ljR05ldVBVRkRUbFQzb0xZLzBNVkhWU2VkL2Z0bGZZT0s1Q2h6NA==|b6bd470987398efe10d140414113720297f8e42cf4f337b67f8abcfc0039775f; SESSIONID=JfWFnK9cwkAy6djCeToAo1wTbiYoTLJZcu28kWw9iSC; JOID=UVkTAEi_oaGaqfNdAb6zNpXEtbsc98Dz3Me6Y2fIyOfmn5c1RcgAA_yr9l8E0oKYrEj0esV5zzSnEPsd91JXqm8=; osd=VF0cB0u6pa6dqvZZDrmwM5HLsrgZ88_038K-bGDLzePpmJQwQccHAPmv-VgH14aXq0vxfsp-zDGjH_we8lZYrWw=; gdxidpyhxdE=%5CNxE9WjII1lsJS%2FdA8sME%2BocVe5UourlOhk0krkAoN%2FXtZeT3IyYO3%2BwjHxN%5CYocnbXxMYXpw3LsG9BDtG7dTthNLQp0ar%5C1c3athak2xIOoC3ZZpkyYLspNrJ%2BYUSskH%2BlOev8vchDIAaRJh%5Ci1p%5C0ctTc9HXukuj8CPYjS1kIpEOaw%3A1722263287443; captcha_ticket_v2=2|1:0|10:1722262401|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfRUNUZU82TUVvYlV4V1lzd09yMHluRDRuZ1Z1QUNYTVlKbk1WWlMzbFpxdXpLeW5DMkRSVWVyNHZSdSpSc3FYTmpFVFJDWGlFTklvU3pfZDNxV0taU3lhQVFrRFR2bVZlLktWOWRJa3ExaVNBbmxIZFFYbjN4Z0M4Ujg0OGtBbU9RVDR0dE9XSHZzbnBfaFVxT3pob3QyRlhzQmdEemY1VnBseDk5WUdzYmUzLkl2TEFhQ3IuY2xoOFRrRjU0Z0lVRkFUSEd5b3lQS29XNkxKeXhPQmtKeXFOZnVTRkFVT29rSFRpbnZpNlg2QWZUcG5wVmJ5LlJjR2x6MW4ydWp0bi5TblFNaGVjbjRTV0cudkVQc2NMd05QdWd3ZXNCQjZiUExBSGNTM3NWZ3J3Ujh4VFNiLmFRampCViozTTkxbmd0VV9udWoxayplcWpDVVdxNlBtczVaVEsqR3NGNERVV3FDajQzV2t5bGFXR2pYZU14Zzg0eC5DQUlYTW00bG1EbkJnYVpRRmZqUHJBelhfMFpwREFrUFBuaGpVVGF5V0t1eUtTdXlyZUdreUJtOW1KTWFGVzlOb1pEOW1GZzU2cXZSTEhDdWtGdUdHVEZ6emk1QjVGUjVrb3lSOFAybWwzX042QWs2OENVUEFRTVBVcEtzQUlmMWtqTDhHcnQ5aC42V2hYQVg3N192X2lfMSJ9|0bc4eb5e6aeebfc713221f537c3fd5d9716611a117630ca267c77d0db6b208d4; z_c0=2|1:0|10:1722262418|4:z_c0|92:Mi4xczFPZ0lRQUFBQUFBUUJLcFowYmtHQ1lBQUFCZ0FsVk5rdkdVWndDdThveGstSWpqa0RNeXFZTEtQZDVxXy1HdXR3|a868cfc71c9e673bf3d9d72c03884e6da936a44a9bad508fb8a94284022ecbe7; q_c1=d77241c4f26d4bddae07d6ce05167b08|1722262419000|1722262419000; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1722262420; tst=r; BEC=244e292b1eefcef20c9b81b1d9777823',
    jar = requests.cookies.RequestsCookieJar()
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
    print(r.text)
    print(r.content)


# 新建了一个RequestCookieJar对象 之后将复制的cookies通过split()分割之后利用set()设置好每一个cookie的key和value


# fun_requests_use_cookies_test()

# 会话维持
# 1.保持每一次请求都是一样的cookies
# 2.维持同一个会话

def fun_session_test():
    import requests

    # 两次请求cookies不同
    r = requests.get('http://httpbin.org/cookies/set/number/123456789')
    print(r.text)
    r = requests.get('http://httpbin.org/cookies')
    print(r.text)
    print('使用session')
    # 使用sesion
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


#     session可以用来模拟在一个浏览器中打开同意站点的不同页面

# fun_session_test()


# SSL证书验证
# 发送http请求的时候它会检查SSL证书
# verify参数控制是否检查此证书  默认为True 自动验证

def fun_ssl_test():
    import requests

    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)
    #     or 通过捕获警告到日志->忽略警告
    import logging
    logging.captureWarnings(True)
    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)
    #     or 指定一个本地证书 作为客户端证书->单个文件（包含密钥和证书）或者一个包含两个文件路径的元组
    response = requests.get('http://www.12306.cn', cert=('/path/server.crt', 'path/key'))
    print(response.status_code)  # 本地的私有证书的key为解密状态


# fun_ssl_test()


# 代理设置
# 使用proxies参数设置代理
def fun_daili_test():
    import requests

    proxies = {
        # 例子
        # "http": "http://10.10.1.10:3128",
        # "https": "http://10.10.1.10:1080"

        # 若代理使用HTTP Basic Auth 则可以使用类似http://user:password@localhost:port
        # "http": "http://user:password@10.10.1.10:3128",
        # requests还支持SOCKS协议的代理
        # pip install 'requests[socks]'
        # 'http':'sockss://user:password@host:port',
        # 'https': 'sockss: // user: password @ host:port'
    }
    requests.get("https://www.taobao.com", proxies=proxies)


# fun_daili_test()

# 超时设置
def fun_timeout_test():
    import requests

    r = requests.get('http://www.taobao.com', timeout=1)
    print(r.status_code)
    # 请求分为两个阶段 连接connect 读取read timeout = time(connect+read)
    # timeout=(5,11,30)传入元组粉分别指定
    # None默认值 -> 永久等待


# fun_timeout_test()


# 身份认证
# 使用requests自带的身份认证功能
def fun_authbasic_test():
    import requests
    from requests.auth import HTTPBasicAuth

    r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
    # or 直接传入元组 默认使用HTTPBasicAuth类来认证
    r = requests.get('http://localhost:5000', auth=('username', 'password'))
    # 或者通过OAuth认证 安装oauth
    # pip install requests_oauthlib
    # from requests_oauthlib import OAuth1
    # url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    # auth = OAuth1('YOU_APP_KEY','YOU_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
    # requests.get(url, auth=auth)
    print(r.status_code)


# fun_authbasic_test()

# Prepared Request
# 将请求表示为数据结构  每一个参数都可以通过一个Request对象来表示
def fun_preparedrequest_test():
    from requests import Request, Session
    url = 'http://httpbin.org/post'
    data = {
        'name': 'germey'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    s = Session()
    req = Request('POST', url, data=data, headers=headers)
    prepped = s.prepare_request(req) # 将其转换为Prepared Request对象
    r = s.send(prepped) # 再调用send方法发送
    print(r.text)
#     通过Request 可以将请求作为独立的对象来看待 这样可以用来构造Request队列
fun_preparedrequest_test()
