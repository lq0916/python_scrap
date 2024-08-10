"""
Title:pyquery库的使用
Author:无医
Time:2024/8/4 
"""


def fun_test():
    from pyquery import PyQuery as pq  # 引入模块 并 取别名
    import requests
    html = '''
    <div>
    <ul>
    <li class="item-0" name="lq01"><a href="link1.html">first item</a>
    <li class="item-1"><a href="link2.html">second item</a>
    <li class="item-inactive"><a href="link3.html">third item</a>
    <li class="item-1"><a href="link4.html">fourth item</a>
    <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
    </div>
    '''
    doc = pq(html)  # 字符串初始化
    print(doc('li'))
    doc = pq(url='https://cuiqingcai.com')  # url初始化
    doc = pq(requests.get('https://cuiqingcai.com').text)  # 与上面一行等效
    doc = pq(filename='#')  # 文件初始化
    print(doc('title'))


# fun_test()

# CSS选择器
def fun_css_test():
    html = '''
    <div id="container">
    <ul class="list">
    <li class="item-0" name="lq01"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a><li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></i>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    </div>
    '''

    from pyquery import PyQuery as pq
    doc = pq(html)
    print(doc('#container .list li'))
    print(type(doc('#container .list li')))

    # 查找节点
    print("子节点")
    items = doc('.list')
    print(type(items))
    print(items)
    lis = items.find('li')  # 查找节点的所有子孙节点
    print(type(lis))
    print(lis)
    lis = items.children()  # 查找子节点
    print(type(lis))
    print(lis)
    lis = items.children('.active')  # 查找子节点
    print(type(lis))
    print(lis)
    print("父节点")
    container = items.parent()
    print(type(container))  # 直接父节点
    print(container)
    parents = items.parents()  # 祖先父节点返回全部祖先节点 可以传入CSS选择器
    print(type(parents))
    print(parents)
    # 兄弟节点
    print("兄弟节点：")  # siblings()方法
    li = doc('.list .item-0.active')
    print(li.siblings())  # 可以传入CSS选择器
    print(li)
    print("遍历：")
    for item in li.siblings().items():
        print(item)
    print("获取属性：")
    a = doc('.item-0.active a')
    print(a, type(a))
    print(a.attr('href'))  # a.attr.href
    print("读取文本：")
    print(a.text())  # 若获取节点内部的HTML文本  则使用html()方法
    # 多个节点时 html返回第一个  text返回全部（空格间隔）
    # 遍历
    a = doc('a')
    print("遍历获取")
    for item in a.items():
        print(item.attr('href'))


# fun_css_test()


# 节点操作

def fun_test_1():
    html = '''
    <div class="wrap">
    <div id="container">
    <ul class="list">
    <li class="item-0" name="lq01"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a><li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></i>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    </div>
    </div>
    '''
    # 动态改变class的属性
    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('.item-0.active')
    print(li)
    li.remove_class('active')
    print(li)
    li.add_class('active')
    print(li)

    print("改变节点内部的内容：")
    li = doc('.item-0.active')
    print(li)
    li.attr('name', 'link')
    print(li)
    li.text('changed item')
    print(li)
    li.html('<span>changed ite</span>')
    print(li)


# fun_test_1()

def fun_remove_test():
    html = '''
    <div class="wrap">
        Hello, World
    <p>This is a paragraph.</p>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    wrap = doc('.wrap')
    print(wrap.text())  # 包含p节点
    wrap.find('p').remove()
    print(wrap.text())


# fun_remove_test()

def fun_test_wei():
    html = '''
    <div class="wrap">
    <div id="container">
    <ul class="list">
    <li class="item-0" name="lq01"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a><li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></i>
    <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    </div>
    </div>
    '''
    from pyquery import PyQuery as pq
    doc = pq(html)
    li = doc('li:first-child') # 第一个
    print(li)
    li = doc('li:last-child')  # 最后一个
    print(li)
    li = doc('li:nth-child(2)')  # 第二个
    print(li)
    li = doc('li:gt(2)')  # 第三个li之后的li节点
    print(li)
    li = doc('li:nth-child(2n)')  # 偶数位置的li节点
    print(li)
    li = doc('li:contains(second)')  # 包含secon文本的li节点
    print(li)

fun_test_wei()





