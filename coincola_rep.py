# -*- coding:utf-8 -*-sanic
# Python3
# File    : coincola
# Time    : 2017/12/26 11:26
# Author  : Shaweb
import time
from email.header import Header
from email.mime.text import MIMEText
from pprint import pprint
from smtplib import SMTP

import requests
from bs4 import BeautifulSoup


def query_price(coin, buy_or_sell):
    url = "https://www.coincola.com/{buy_or_sell}/{coin}?country_code=CN".format(buy_or_sell=buy_or_sell, coin=coin)
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        tr = soup.find("tbody").find_all('tr')
    except Exception as e:
        return None, e

    results = {}
    ETH_sell_infos = []
    price_list = []

    for i in tr:
        o = {}
        o['price'] = float(i.find("td", "td-price").text.split(' ')[0])
        price_list.append(o['price'])
        o['pay_way'] = i.find_all('td')[2].text
        o['limit'] = i.find_all('td', 'td-name')[1].text
        o['url'] = "https://www.coincola.com" + i.find('a', 'btn submit')['href']
        ETH_sell_infos.append(o)
    print(len(ETH_sell_infos))
    current_highest_price = price_list[0]
    pre_avg = price_list[:8]
    avg_price = round(sum(pre_avg) / len(pre_avg), 2)

    results['current_highest_price'] = current_highest_price
    results['avg_price'] = avg_price
    results['infos'] = ETH_sell_infos

    return results, None


def send_email(SMTP_host="smtp.163.com",
               nick_name="按时汇报的可乐",
               from_account="shwb95@163.com",
               from_passwd="****",
               to_account="584927688@qq.com",
               title="CoinCola",
               content=""):
    email_client = SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    HTML = "{}<p>----可乐于{}如是向主人汇报</p>".format(content, now)

    msg = MIMEText(HTML, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(title, 'utf-8')  # subject
    msg['From'] = nick_name
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


def coincola_worker(expect_sell_high_price=5800):
    while True:
        result, err = query_price("ETH", "sell")
        if err:
            send_email(title="coincola请求失败", content="coincola请求失败")
        avg_price = result.get("avg_price")
        current_highest_price = result.get("current_highest_price")
        infos = result.get("infos")

        HTML = "<table border=\"1\"><tr><th>序号</th><th>限额</th><th>交易方式</th><th>价格</th></tr>{}</table>"
        tr = ""
        for index, i in enumerate(infos):
            way = i.get("pay_way")
            price = i.get("price")
            limit = i.get("limit").split(' ')[0]
            url = "<a href=\"{}\">".format(i.get("url"))
            tr += "<tr><td>{}</td>\<td>{}</td><td>{}</td>\<td>{}{}</td></tr>".format(index, limit, way, url, price)

        content = "<p>最高价：{}</p><p>前8平均价：{}</p>{}".format(current_highest_price, avg_price, HTML.format(tr))
        if avg_price >= expect_sell_high_price:
            send_email(title="主人，收购价格涨到5800啦！",
                       content=content)
        else:
            send_email(title="主人，ETH现在{}收购了！".format(current_highest_price),
                       content=content)

        time.sleep(60*10)


# if __name__ == '__main__':
#    pprint(query_price("ETH", "sell"))
    # send_email()
    # coincola_worker()


# --------------------------------------

# -*- coding:utf-8 -*-
# Python3
# File    : app
# Time    : 2017/12/26 13:10
# Author  : Shaweb
import json

from flask import Flask, request, Response

from coincola import query_price

app = Flask(__name__)


def returnjsonresp(respbody):
    resp = Response(json.dumps(respbody))
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/')
def test():
    return "ok"

@app.route('/coincola')
def coincola():
    coin = request.args.get('coin').upper()
    do_what = request.args.get('do')
    result,err = query_price(coin,do_what)
    if err:
        return returnjsonresp({'result': '', 'error': True, 'info': err})

    return returnjsonresp({'result': result, 'error': False, 'info': ''})

if __name__ == '__main__':
    # app.run(host='127.0.0.1',
    #         port=12301,
    #         # threaded=True,
    #         # debug=True
    #         )
