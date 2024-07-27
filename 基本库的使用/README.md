不要阅读我

urllib 库 的使用

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