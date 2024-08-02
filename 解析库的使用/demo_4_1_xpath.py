"""
Title:解析库的使用
Author:无医
Time:2024/8/2 
"""


# XPath -> XML Path Language
# //title[@lang='eng']  -> 选择所有名称为title 且属性值lang = eng 的节点

def fun_test():
    from lxml import etree
    import re

    text = '''
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
    html = etree.HTML(text)
    # 所有节点
    result = html.xpath('//*')
    # 所有li节点
    result_li = html.xpath('//li')
    print("所有节点", result)
    print("所有li节点", result_li)
    print("第一个li节点", result_li[0])

    # 子节点   /   //
    print("子节点：")
    result_zi = html.xpath('//li/a')  # //ul/a ul节点下的所有子孙a节点
    # / 用于获取直接子节点 //用于获取子孙节点
    print("获取li节点的直接a子节点", result_zi)

    # 父节点    ..
    print("父节点")
    result_fu = html.xpath('//a[@href="link4.html"]/../@class')
    result_fu_1 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    print(result_fu)
    print(result_fu_1)

    # 属性匹配
    print("属性匹配:")
    result_pipei = html.xpath('//li[@class="item-0"]')
    print(result_pipei)

    # 文本获取
    print("文本获取:")
    result_text = html.xpath('//li[@class="item-0"]/a/text()')
    result_text_ = html.xpath('//li[@class="item-0"]//text()')
    print(result_text)
    print(result_text_)

    # 属性获取 <->属性匹配 带有中括号[@href = "link1.html"]
    print("属性获取:")
    result_shuxing = html.xpath('//li/a/@href')
    print(result_shuxing)

    # 属性多值匹配 contain(属性名称 , 属性值)
    print("属性多值匹配:")
    text = '''
    <li class="li li-first name="item" ><a href="link.html">first item</a></li>
    '''
    html1 = etree.HTML(text)
    result1 = html1.xpath('//li[contains(@class,"li")]/a/text()')
    print(result1)

    # 多属性匹配
    print("多属性匹配")
    result2 = html1.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
    print(result2)

    # 按序选择
    print("按序选择:")
    result = html.xpath('//li[1]/a/text()')
    print(result)
    result = html.xpath('//li[last()]/a/text()')
    print(result)
    result = html.xpath('//li[position()<3]/a/text()')
    print(result)
    result = html.xpath('//li[last()-2]/a/text()')
    print(result)

    # 节点轴选择
    print("节点轴选择:")
    result = html.xpath('//li[1]/ancestor::*') # 获取所有祖先节点*
    print(result)
    result = html.xpath('//li[1]/ancestor::div') # 获取所有祖先div节点
    print(result)
    result = html.xpath('//li[1]/attribute::*') # 获取所有节点的属性值
    print(result)
    result = html.xpath('//li[1]/child::a[@href="link1.html"]') # 获取直接子节点
    print(result)
    result = html.xpath('//li[1]/descendant::*') # 获取所有子孙节点
    print(result)
    result = html.xpath('//li[1]/following::*[last()]') # 获取当前节点之后的所有节点
    print(result)
    result = html.xpath('//li[1]/following-sibling::*') # 获取当前节点之后的所有同级节点
    print(result)
    result_ = etree.tostring(html)
    print(result_.decode('utf-8'))


fun_test()
