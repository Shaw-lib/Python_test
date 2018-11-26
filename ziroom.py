# -*- coding:utf-8 -*-
# Python3
# File    : helps
# Time    : 2017/9/22 14:23
# Author  : Shaweb

import datetime
import time
from pprint import pprint

import requests


def search_ziroom(key):
    while True:
        print('start %s %s ' % ('key', datetime.datetime.now()))
        for i in range(0, 901, 10):
            payload = {'step': i,
                       'recent_money': 3,
                       'sort': 2,  # 价格从低到高
                       'room': 3,  # 三居室
                       'key_word': key}
            headers = {'Referer': 'http://m.ziroom.com/BJ/search.html',
                       'Host': 'm.ziroom.com',
                       'Origin': 'http://m.ziroom.com',
                       'Proxy-Connection': 'keep-alive',
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
            res = requests.post('http://m.ziroom.com/list/ajax-get-data', data=payload, headers=headers)
            if 'info' in res.json()['data'] and res.json()['data']['info'] == '数据加载完毕':
                print('到底了~')
                break
            data = res.json()['data']
            result = {}
            for item in data:
                status = item.get('room_status')
                if status == 'yxd':
                    result['status'] = '已预订'
                    continue

                result['id'] = item.get('id')
                result['key'] = key
                result['name'] = item.get('room_name')
                result['img'] = item.get('list_img')
                result['url'] = "http://www.ziroom.com/z/vr/{}.html".format(item.get('id'))
                result['price'] = item.get('sell_price')
                result['area'] = str(item.get('usage_area')) + '平米'
                result['distance'] = item.get('walking_distance_dt_first')
                result['house'] = item.get('dispose_bedroom_amount') + '居室'

                if status == 'tzpzz':
                    result['status'] = '配置中'
                elif status == 'dzz':
                    result['status'] = '可签约'
                pprint(result)

            time.sleep(3)
        print('-----------')
        time.sleep(20 * 60)


if __name__ == '__main__':
    search_ziroom('青年路')
