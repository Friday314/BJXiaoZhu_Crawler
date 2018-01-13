# 导入库文件
from bs4 import BeautifulSoup
import time
import requests


# 请求头文件
_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
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
            "tittle" :tittle.get_text().strip(),
            "addresse" :addresse.get_text().strip(),
            "price" :price.get_text(),
            "img" :img.get("url"),
            "name" :name.get_text(),
            "sex" :_sex(sex.get("class"))
        }

        print(data)



urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number)
        for number in range(1,11)]

for single in urls:

    # get_links(single)

    r = requests.get(single, headers=_headers)
    soup = BeautifulSoup(r.text, "lxml")
    # links = soup.select("#page_list > ul > li > a")
    links = soup.select("# page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > span.result_img > a")


    for link in links:

        print(link)

        # herf = link.get("herf")
        # get_info(herf)

        wb_data = requests.get(link, headers=_headers)

        soup = BeautifulSoup(wb_data.text, "lxml")

        tittles = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4")
        addresses = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span")
        prices = soup.select("#pricePart > div.day_l > span")
        imgs = soup.select("#curBigImage")
        names = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")
        sexs = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")

        for tittle, addresse, price, img, name, sex in zip(tittles, addresses, prices, imgs, names, sexs):
            data = {
                "tittle": tittle.get_text().strip(),
                "addresse": addresse.get_text().strip(),
                "price": price.get_text(),
                "img": img.get("url"),
                "name": name.get_text(),
                "sex": _sex(sex.get("class"))
            }

            print(data)

    time.sleep(2)
