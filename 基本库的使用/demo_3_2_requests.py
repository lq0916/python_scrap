"""
Title:
Author:无医
Time:2024/7/28 
"""

# 基本使用  安装 pip install request
# urllib 中urlopen 以Get方式请求网页  ->request get方法
# 获取的为Response对象
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
# fun_request_test()

# GET 请求
# get->简单的实例
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
