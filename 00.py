# 导入库文件
import requests
import time
from bs4 import BeautifulSoup

# 请求头文件
_headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def _sex(class_name):

    """
    定义判断用户姓名的函数
    :rtype: object
    """

    if class_name == ["member_ico1"]:
        return "女"
    else:
        return "男"


def get_links(usr):

    """
    定义获取详细页URL的函数
    :param usr:
    """

    # page_list > ul > li:nth-child(1) > div.result_btm_con.lodgeunitname
    # page_list > ul > li:nth-child(2) > div.result_btm_con.lodgeunitname > div > a

    r = requests.get(usr, headers=_headers)
    soup = BeautifulSoup(r.text, "lxml")
    links = soup.select("#page_list > ul > li > a")

    for link in links:
        herf = link.get("herf")
        get_info(herf)


def get_info(url):
    wb_data = requests.get(url, headers=_headers)
    soup = BeautifulSoup(wb_data.text, "lxml")
    tittles = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4")
    addresses = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span")
    prices = soup.select("#pricePart > div.day_l > span")
    imgs = soup.select("#curBigImage")
    names = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")
    sexs = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")

    for tittle, addresse, price, img, name, sex in zip(tittles, addresses, prices, imgs, names, sexs):
        data = {
            "tittle" : tittle.get_text().
        }
