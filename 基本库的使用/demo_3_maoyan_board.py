"""
Title:爬取猫眼排行榜
Author:无医
Time:2024/7/31 
"""
# url = 'http://maoyan.com/board/4'
# 通过解析 可知 offset 参数 为偏移量
# offset 0->90 即可
# 引入库
import requests
import json
from requests.exceptions import RequestException
import re
import time


# 获取网页代码
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 匹配需要信息
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)  # 匹配数据
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    # 尾端添加为验证测试
    url = 'http://maoyan.com/board/4?offset=' + str(offset)+'&requestCode=ba5c904173b18c01135999d7888a5588c25kl'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(2)

# 分析network中的html代码之后可以获取到每一个影片的相关信息是在一个dd标签当中 之后分析完成相应的正则表达式
# 排名 <dd>.*?board-index.*?>(.*?)</i>
# 图片 <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
# 名称 <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>
# 总:  <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>
