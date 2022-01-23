# 樵夫专场
# 我们一起手拉手, 一起走向刑场

# 用爬虫的技术. 抓取微博的评论信息

#  1.检查你要得东西在不在页面源代码里面
#    如果在的话. 就简单了. 直接requests.get()
#    如果不在. 当前要的东西。 一定是一个异步加载
#  微博评论是异步加载的
#  所有的异步请求都要去看抓包工具。
#    大概率你要的东西在xhr那一档

# 微博是这样的：
# 1.先加载一个框框
# 2.加载评论信息。
#   通过脚本 把评论信息塞入到上面的框框中 。

# https://weibo.com/6336553950/LbNd7mdIm?type=comment
# mid

import time
import requests  # pip install requests
import re
from lxml import etree  # pip install  lxml



# 整体处理思路:
# 1. 访问页面源代码. 拿到mid
# 2. 用mid发送请求. 获取到第一页数据
# 3. 留个悬念.

headers = {
    # 请自行更换成自己的cookie进来
    "cookie": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}


def get_mid(url):  # 某个需要评论信息的url
    resp = requests.get(url, headers=headers)
    # 正则表达式 re模块
    mid_re = re.compile(r"mid=(?P<mid>\d+)")
    mid = mid_re.search(resp.text).group("mid")  # 提取mid的值
    print(mid)  # 4728107775295938
    return mid


# 提取评论信息
def get_common(mid, ref_url):
    # 微博评论的url
    url = "https://weibo.com/aj/v6/comment/big"
    params = {
        "ajwvr": 6,  # 顶死
        "id": mid,  # 变化 可以从页面源代码里拿到
        "from": "singleWeiBo",  # 顶死
        "__rnd": int(time.time() * 1000)  # 变化的 时间戳
    }
    # 请求头和之前的请求头不一样
    headers["referer"] = ref_url
    headers['x-requested-with'] = "XMLHttpRequest"
    n_url = url  # 为了后面的逻辑. 不得不搞一个这个.
    while 1:
        resp = requests.get(n_url, params=params, headers=headers)
        # print(resp.text)  # 第一页的评论信息
        # 解析第一页的评论信息.
        # 先把微博评论的json还原回字典
        html = resp.json()['data']['html']
        # print(html)

        # 处理获取到的html. 从中提取到评论信息
        n_url = url + "?" + process_common(html)


def process_common(hm):
    # 用xpath提取数据
    tree = etree.HTML(hm)
    divs = tree.xpath("//div[@class='list_box']/div/div[@node-type='root_comment']")
    for div in divs:  # div就是每一个评论
        comment_id = div.xpath("./@comment_id")
        user = div.xpath("./div[2]/div[1]/a/text()")
        content = div.xpath("./div[2]/div[1]/text()")

        # 把提取到的数据进行处理
        content = "".join(content).strip().strip("：")  # 这里千万千万要复制
        user = user[0]
        comment_id = comment_id[0]
        print(comment_id, user, content)  # xlwt openpyxl
        f.write(comment_id)
        f.write("|||")  # 分隔符
        f.write(user)
        f.write("|||")  # 分隔符
        f.write(content)
        f.write("\n")

    # 第二页????
    # 拿到action_data, 补齐(aw, __rnd, from)
    action_data = tree.xpath("//div[@node-type='comment_loading']/@action-data")
    if action_data:   # 如果这里拿不到action-data
        url = action_data[0]
        url += "&__rnd="+str(int(time.time()*1000))
        url += "&ajwvr=6"
        url += "&from=singleWeiBo"
        return url
    # 找a, click_more_comment  同样的提取它的 actino-data
    # if xxx:
    #     url = action_data[0]
    #     url += "&__rnd=" + str(int(time.time() * 1000))
    #     url += "&ajwvr=6"
    #     url += "&from=singleWeiBo"
    #     return url
    # return None


# 准备文件夹
f = open('评论.txt', mode="w", encoding="utf-8")
url = "https://weibo.com/6336553950/LbNd7mdIm?type=comment"
mid = get_mid(url)
get_common(mid, url)
f.close()
