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


def get_links(url):
    """
    定义获取详细页URL的函数
    :param url:
    """
    r = requests.get(url, headers=_headers)
    soup = BeautifulSoup(r.text, "lxml")
    links = soup.select("#page_list > ul > li > a")

    for link_url in links:

        # print(link.get("href"))
        get_info(link_url)



def get_info(url):
    """
    定义获取网页信息的函数
    :param url:
    """
    wb_data = requests.get(url.get("href"), headers=_headers)

    soup = BeautifulSoup(wb_data.text, "lxml")

    # print(soup)

    tittles = soup.select("div.pho_info > h4")
    addresses = soup.select("span.pr5")
    prices = soup.select("#pricePart > div.day_l > span")
    imgs = soup.select("#curBigImage")
    names = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")
    sexs = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")

    for tittle, addresse, price, img, name, sex in zip(tittles, addresses, prices, imgs, names, sexs):
        data = {
            "标题": tittle.get_text().strip(),
            "地址": addresse.get_text().strip(),
            "租金": price.get_text(),
            "图片": img.get("src"),
            "用户": name.get_text(),
            "性别": _sex(sex.get("class"))
        }

        print(data)


# main 函数
if __name__ == "__main__":

    #构造多页URL

    urls = ["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(number) for number in range(1,11)]

    for single in urls:

        get_links(single)

        # 睡眠两秒
        time.sleep(2)
