不要阅读我

# urllib 库 的使用

request:最基本的http请求模块
error:异常处理模块
parse:工具模块  提供许多url的处理方式
robotparser:识别网上的robots.txt


## 解析链接
>urllib库中提供了parse模块  定义url的标准接口
>例如实现url 各部分的抽取 合并 链接转换

### 1.urlparse()
  ->实现url的识别和分段
  ->返回ParseResult类型对象: scheme  netloc path params query fragment
  ->返回对象实际上为一个元组 可以根据 索引顺序获取 或者根据属性名获取
**urlparse(url, scheme='', allow_fragments=True)**
>url 待解析的url 
>scheme默认协议 若链接没有带协议信息 则将其作为默认协议 若有则不生效
>allow_fragments是否忽略fragment  false则忽略fragment 将其解析为 path params query
```python
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
```
![img.png](../image/img.png)
### 2.urlunparse()
>urlparse()对立方法   接受参数是一个可迭代的对象 长度为6 否则 抛出异常
```python
def fun_urlunparse_test():
    from urllib.parse import urlunparse

    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urlunparse(data))
# fun_urlunparse_test()
```
### 3.urlsplit()
>与urlparse相似 不单独解析params 返回五个结果 将params 合并的path中
>同理亦可 根据索引或属性名
```python
def fun_urlsplit_test():
    from urllib.parse import urlsplit

    result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
    print(len(result),result,sep='\n')
    print("由索引顺序,或者属性名")
    print(result[0],result.scheme,result[1],result.netloc,sep='\n')
# fun_urlsplit_test()
```
### 4.urlunsplit()
>与urlunparse()相似 不赘述
```python
def fun_urlunsplit_test():
    from urllib.parse import urlunsplit

    data = ['http', 'www.baidu.com', 'index.html','a=6', 'comment']
    print(urlunsplit(data))
# fun_urlunsplit_test()
```
### 5.urljoin()
> 有了urlunparse 和 urlunsplit 则可根据定长对象完成合并
> urljoin 采用 base_url作为第一参数 将新的链接作为第二个参数  方法会分析base_url的scheme  netloc path 对新链接缺失的内容进行补充
```python
def fun_urljoin_test():
    from urllib.parse import urljoin

    print(urljoin('http://www.baidu', 'FAQ.hitml'))
    print(urljoin('http://www.baidu', 'http://www.cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu/about.html', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu/about.html','http://www.cuiqingcai.com/FAQ.html?qestion=2'))
    print(urljoin('http://www.baidu.com','?category=2#comment'))
    print(urljoin('www.baidu.com#comment','?category=2'))
# fun_urljoin_test()
```
### 6.urlencode()
> 用于构造get请求参数
> 使用字典将参数表示出来  之后调用方法 将其序列化为get请求参数

```python
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
```


### 7.parse_qs
> 反序列化 <-> urlencode
> 将get请求转为字典
> 
```python
def fun_parse_qs_test():
    from urllib.parse import parse_qs

    query = 'name=germey&age=22'
    print(parse_qs(query))
fun_parse_qs_test()
```

### 8.parse_qsl()
> 将参数转化为元组组成的列表
```python
def fun_parse_qsl_test():
    from urllib.parse import parse_qsl
    query = 'name=germey&age=22'
    print(parse_qsl(query)) 
    # [('name', 'germey'), ('age', '22')]
fun_parse_qsl_test()
```

### 9.quote()
> 将内容转换为url编码格式 url带有中文参数的时候可能会导致乱码问题 此时可用此方法
```python
def fun_quote_test():
    from urllib.parse import quote

    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd='+ quote(keyword)
    print(url)
# fun_quote_test()
```

### 10.unquote
> 将url进行解码
```python
def fun_unquote_test():
    from urllib.parse import unquote

    url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    print(unquote(url))
fun_unquote_test()
```

### 分析Robots协议 
>->urllib.robotparser模块
> robots.txt 爬虫协议 网络爬虫排除标准
> 我反正不看 哈哈哈
> 爬虫名称

### robotparser
> 使用该模块解析robots.txt ->RobotFileParser

```python
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
```

# request库的使用

> 基本使用  安装 pip install request
> urllib 中urlopen 以Get方式请求网页  ->request get方法
> 获取的为Response对象
```python
def fun_request_test():
    import requests

    r = requests.get('http://wwww.baidu.com/')
    print(type(r)) # Response对象
    print(r.status_code) # 状态码
    print(type(r.text)) # 响应体的类型
    print(r.text) # 响应体的内容
    print(r.cookies) # Cookies

    # 方便于其他请求类型依然可以使用一句话完成
    r = requests.post('http://httpbin.org/post')
    r = requests.put('http://httpbin.org/put')
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')
fun_request_test()
```


## GET 请求
> get->简单的实例
```python
def fun_Get_test():
    import requests

    r = requests.get('http://httpbin.org/get')
    # 返回结果包括请求头 URL IP等
    print(r.text)
# fun_Get_test()
```

> get->附加参数 使用 params参数
```python
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
```

**>抓取网页**

```python
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
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)# 已经失效需要重新考虑
    titles = re.findall(pattern, r.text)
    print(titles)
# fun_request_scrap_test()
```

**> 抓取二进制数据**
> 上面的案例返回一个html文档

> 抓取github的站点图标
```python
def fun_Scrap_Github_ico_Test():
    import requests

    r = requests.get("https://github.com/favicon.ico")
    # 返回的是Response对象  两个属性 text  content
    print(type(r))
    print(r.text)# 乱码 由于图片是二进制数据  打印为str  则乱码
    print(r.content)# 结果前面带有b -> bytes类型数据
    # 保存图片 ->音频和视频同理
    with open('github_favicon.ico', 'wb') as f:
        f.write(r.content)
# fun_Scrap_Github_ico_Test()
```


## post请求
```python
def fun_post_test():
    import requests
    data = {'name': 'germey', 'age': '22'}
    r = requests.post("http://httpbin.org/post", data=data)
    print(r.text)  # 返回结果中form部分为提交的数据


# fun_post_test()
```

**> 响应**
> 发送请求之后获得响应  再上面的实例中我们使用了text和content
> 此外还有很多的属性方法 requests.Response

```python
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


fun_requests_get_test()
```


> 高级用法

**> 文件上传**
```python
def fun_file_post_test():
    import requests

    files = {'file': open('github_favicon.ico', 'rb')}
    r = requests.post("http://httpbin.org/post", files=files)
    print(r.text)
    # 响应头中会包含files这个字段  form字段是空的
    # fun_file_post_test()
```


**> Cookies->获取cookies**
```python
def fun_requests_cookies_test():
    import requests

    r = requests.get("http://www.baidu.com")
    print(r.cookies)  # Cookies为RequestsCookieJar类
    for key, value in r.cookies.items():
        print(key + '=' + value)


# fun_requests_cookies_test()
```

**> 使用cookies**
```python
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
```
**> 会话维持**
> 1.保持每一次请求都是一样的cookies
> 2.维持同一个会话

```python
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

fun_session_test()
```


**> SSL证书验证**
> 发送http请求的时候它会检查SSL证书
> verify参数控制是否检查此证书  默认为True 自动验证

```python
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
```


**> 代理设置**
> 使用proxies参数设置代理
```python
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
```

**> 超时设置**
```python
def fun_timeout_test():
    import requests

    r = requests.get('http://www.taobao.com', timeout=1)
    print(r.status_code)
    # 请求分为两个阶段 连接connect 读取read timeout = time(connect+read)
    # timeout=(5,11,30)传入元组粉分别指定
    # None默认值 -> 永久等待


# fun_timeout_test()
```

**> 身份认证**
> 使用requests自带的身份认证功能
```python
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


fun_authbasic_test()
```

**> Prepared Request**
> 将请求表示为数据结构  每一个参数都可以通过一个Request对象来表示
```python
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
```

# 正则表达式
> 通过正则表达 处理字符串 ->
> 检索 替换 匹配验证
> 在线正则表达式使用
>http = 'http://tool.oschina.net/regex/'
> 匹配URL -> [a-zA-z]+://[^\s]*   \s表示匹配任意的空白字符 *表示前面的字符任意多个
![img.png](../image/img_re_guize.png)
>正则表达式  非独有 在python中使用re库 


## match()方法使用 -> 从字符串的开头开始匹配
```python
def fun_match_test():
    import re

    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    # 第一参数 正则表达式  第二参数 匹配的字符串
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)
    print(result.group())  # 输出匹配到的内容
    print(result.span())  # 输出匹配的范围  计结果在原字符串中的位置范围


# fun_match_test()
```
**> 匹配目标**
```python

def fun_match__test_1():
    import re

    content = 'Hello 1234567 World_This is a Regex Demo'
    # 第一参数 正则表达式  第二参数 匹配的字符串
    result = re.match('^Hello\s(\d+)\sWorld', content)  # 使用括号将想要提取的字符串括起来 被标记的子表达式对应每一个分组

    print("Result:", result)
    print(result.group())
    print(type(result.group()))
    print('group(0)', result.group(0))
    print('group(1)', result.group(1))
    print(result.span())


fun_match__test_1()
```

**> 通用匹配**
> 万能匹配 .*  -> 匹配任意字符
> . ->任意字符（除换行符） * ->表示匹配前面的字符无限次

```python
def fun_wanneng_test():
    import re
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello.*Demo$', content)  # $ ->匹配一行字符的结尾
    print(result)
    print(result.group())
    print(result.span())


fun_wanneng_test()
```

**> 使用万能匹配 ->  贪婪婪匹配**
```python
def fun_wanneng_tan_test():
    # 获取content中间的数字
    import re
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^He.*(\d+).*Demo$', content)
    print(result)
    print(result.group(1)) # -> 7

# 贪婪匹配下 .*会匹配尽可能多的字符 ->不便
# fun_wanneng_tan_test()
```

> 万能匹配  ->    非贪婪匹配
```python
def fun_wanneng_notan_test():
    import re

    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^He.*?(\d+).*Demo$', content)
    print(result)
    print(result.group(1)) # -> 1234567

    # 不便
    content1 = 'http://weibo.com/comment/kEraCN'
    result1 = re.match('http.*?comment/(.*?)', content1)
    result2 = re.match('http.*?comment(.*)', content1)
    print('result1', result1.group(1)) # 如果匹配结果在字符串结尾 就可能匹配不到任何内容了
    print('result2', result2.group(1))


# 非贪婪匹配下 .*会匹配尽可能少的字符
# fun_wanneng_notan_test()
```

**> 修饰符**
> 正则表达式 可以含一些可选标志修饰符来控制匹配模式 修饰符被指定为一个可选的标志

```python
def fun_xiushi_test():
    import re

    # 添加换行符号
    content = '''Hello 1234567 World_This
     is a Regex Demo'''
    # result = re.match('^He.*?(\d+).*Demo$', content) # result = None
    # print(result.group(1)) # error

    result1 = re.match('^He.*?(\d+).*Demo$', content, re.S)  # re.S使.匹配包括换行符号在内的所有字符
    print(result1.group(1))

fun_xiushi_test()
```
![img.png](../image/img_re_xiushi.png)


> 转义匹配
> 若目标字符串中包含. ->how
```python
def fun_zhuanyi_test():
    import re

    content = '(百度)www.baidu.com'
    result = re.match('\(百度\)www\.baidu\.com', content)
    print(result)
    print(result.group())


# fun_zhuanyi_test()
```

**> search() ->扫描整个字符串 返回第一个成功匹配的结果**
```python
def fun_search_test():
    import re

    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    # result = re.match('Hello.*?(\d+).*?Demo', content)
    # print(result) # result = None
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)
    print(result.group(1))


# fun_search_test()
```

**> 案例测试**
```python
def fun_re_test():
    import re
    html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
    经典老歌列表
    </p>
    <ul id="list" class="list-group">
    <li data-view="2”>一路上有你</li>
    <li data-view="7">
    <a href="/3.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
    <a href="/3.mp3" singer="齐秦">往事随风</a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
    <li data-view="5">
    <a href="/6 .mp3" singer="邓丽君">但愿人长久</a>
    </li>
    </ul>
    </div>'''
    # 提取class为active的li节点内部的超链接包含的歌手名 和 歌名
    result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result:
        print(result.group(1),result.group(2))
    # 不加active
    result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
    if result:
        print(result.group(1), result.group(2))
    # 不加re.S .*不匹配换行符
    result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
    if result:
        print(result.group(1), result.group(2))


# fun_re_test()
```

**> findall()  -> 返回符号要求的全部结果**
```python
def fun_findall_test():
    import re
    html = '''<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
        经典老歌列表
        </p>
        <ul id="list" class="list-group">
        <li data-view="2”>一路上有你</li>
        <li data-view="7">
        <a href="/3.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
        <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
        <a href="/6 .mp3" singer="邓丽君">但愿人长久</a>
        </li>
        </ul>
        </div>'''
    # 返回所有的a节点的超链接
    results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
    # 返回元组列表
    print(results)
    print(type(results))
    for result in results:
        print(result)
        print(result[0], result[1], result[2])


# fun_findall_test()
```
> 获取第一个内容-》search()  获取全部内容 findall()

**> sub()**
> 使用正则表达式 修改文本 若使用repalce()-> 繁琐

```python
def fun_sub_test():
    import re

    content = '54aK54yr5oiR54ix5L2g'
    # sub(匹配参数, 替换为, 原字符串)
    content = re.sub('\d+', '', content)
    print(content)
    html = '''<div id="songs-list">
            <h2 class="title">经典老歌</h2>
            <p class="introduction">
            经典老歌列表
            </p>
            <ul id="list" class="list-group">
            <li data-view="2”>一路上有你</li>
            <li data-view="7">
            <a href="/3.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
            <a href="/6 .mp3" singer="邓丽君">但愿人长久</a>
            </li>
            </ul>
            </div>'''
    # 获取全部li节点的歌名 findall()
    results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
    for result in results:
        print(result[1])
    # sub()方法
    html = re.sub('<a.*?>|</a>', '', html)
    print(html)
    results = re.findall('<li.*?>(.*?)</li>',html,re.S)
    for result in results:
        print(result.strip())
# fun_sub_test()
```

> compile()
> 将正则字符串编译为正则表达式对象  ->有利于后面的匹配复用
```python
def fun_compile_test():
    import re
    content1 = '2016-12-15 12:00'
    content2 = '2016-12-17 12:55'
    content3 = '2016-12-22 13:21'

    pattern = re.compile('\d{2}:\d{2}')

    result1 = re.sub(pattern, '', content1)
    result2 = re.sub(pattern, '', content2)
    result3 = re.sub(pattern, '', content3)
    print(result1, result2, result3, sep='\n')


fun_compile_test()
```

**>案例:猫眼电影排行榜抓取**
> file:demo_3_maoyan_board.py