"""
Title:正则表达式的使用
Author:无医
Time:2024/7/30 
"""

# 通过正则表达 处理字符串 ->
# 检索 替换 匹配验证
# 在线正则表达式使用
http = 'http://tool.oschina.net/regex/'


# 匹配URL -> [a-zA-z]+://[^\s]*   \s表示匹配任意的空白字符 *表示前面的字符任意多个


# match()方法使用 ->从字符串的开头开始匹配
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

# 匹配目标
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


# fun_match__test_1()

# 通用匹配
# 万能匹配 .*  -> 匹配任意字符
# . ->任意字符（除换行符） * ->表示匹配前面的字符无限次

def fun_wanneng_test():
    import re
    content = 'Hello 123 4567 World_This is a Regex Demo'
    result = re.match('^Hello.*Demo$', content)  # $ ->匹配一行字符的结尾
    print(result)
    print(result.group())
    print(result.span())


# fun_wanneng_test()

# 使用万能匹配 ->  贪婪婪匹配
def fun_wanneng_tan_test():
    # 获取content中间的数字
    import re
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^He.*(\d+).*Demo$', content)
    print(result)
    print(result.group(1)) # -> 7

# 贪婪匹配下 .*会匹配尽可能多的字符 ->不便
# fun_wanneng_tan_test()

# 万能匹配  ->    非贪婪匹配
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

# 修饰符
# 正则表达式 可以含一些可选标志修饰符来控制匹配模式 修饰符被指定为一个可选的标志
def fun_xiushi_test():
    import re

    # 添加换行符号
    content = '''Hello 1234567 World_This
     is a Regex Demo'''
    # result = re.match('^He.*?(\d+).*Demo$', content) # result = None
    # print(result.group(1)) # error

    result1 = re.match('^He.*?(\d+).*Demo$', content, re.S)  # re.S使.匹配包括换行符号在内的所有字符
    print(result1.group(1))

# fun_xiushi_test()

# 转义匹配
# 若目标字符串中包含. ->how
def fun_zhuanyi_test():
    import re

    content = '(百度)www.baidu.com'
    result = re.match('\(百度\)www\.baidu\.com', content)
    print(result)
    print(result.group())


# fun_zhuanyi_test()

# search() ->扫描整个字符串 返回第一个成功匹配的结果
def fun_search_test():
    import re

    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    # result = re.match('Hello.*?(\d+).*?Demo', content)
    # print(result) # result = None
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)
    print(result.group(1))


# fun_search_test()

# 案例测试
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

# findall()  -> 返回符号要求的全部结果
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
# 获取第一个内容-》search()  获取全部内容 findall()

# sub()
# 使用正则表达式 修改文本 若使用repalce()-> 繁琐

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

# compile()
# 将正则字符串编译为正则表达式对象  ->有利于后面的匹配复用
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