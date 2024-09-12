import requests
from jsonpath import jsonpath
from openpyxl import workbook
import time
import random

def get_data():
    r = requests.post(url,headers=heardrs,json=playlode)
    if r.status_code == 200:
        # print(type(r.json()))
        return r.json()
    else:
        print(r.status_code)

def jxx(data):
    # print(data)
    title = jsonpath(data,'$..title')
    url2 = jsonpath(data,'$..url')
    tag_words = jsonpath(data,'$..chl_name')
    # print(url2)
    for titles,urls,tag_wordss  in zip(title,url2,tag_words):
        print(f'新闻标题：{titles}\n新闻链接：{urls}\n新闻媒体：{tag_wordss}')
        print('=============='*5)
        save_data(titles,urls,tag_wordss)


def save_data(tit,lin,name):
    ws.append([tit,lin,name])
    wb.save('腾讯新闻.xlsx')

if __name__ == '__main__':
    wb = workbook.Workbook()
    ws = wb.active

    url = 'https://i.news.qq.com/web_feed/getHotModuleList'
    heardrs = {
        'cookie':'RK=gwvBNF6tO3; ptcz=730ae62e10f461f434b2938d6e74f25acb2859f6640602ee4b646bbdfbd8f675; pgv_pvid=1250429676; _qimei_uuid42=1890c0e2f25100a84caa1f52e4120aa3392af06f5f; pac_uid=0_SM2WDY82ADn3S; current-city-name=fuzhou; _qimei_fingerprint=0a18e34c9ba93dc545680d1dbbd15eac; _qimei_q36=; _qimei_h38=e147f4b94caa1f52e4120aa30200000381890c; suid=user_0_SM2WDY82ADn3S; lcad_o_minduid=SWtwqZV2_IvpuYTEOQGHVEynZuRUaDJl; lcad_appuser=60957B3A3CC1B5A5; lcad_Lturn=392; lcad_LKBturn=933; lcad_LPVLturn=654; lcad_LPLFturn=400; lcad_LPSJturn=594; lcad_LBSturn=629; lcad_LVINturn=485; lcad_LDERturn=289',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    for i in range(1,6):
        playlode = {
            'se_req':{'from':"pc"},
            'forward':"2",
            'qimei36':"0_SM2WDY82ADn3S",
            'device_id':"0_SM2WDY82ADn3S",
            'base_req':{'from':"pc"},
            'channel_id':"news_news_top",
            'flush_num':i,
            'item_count':20,
        }
        json_data1 = get_data()
        time.sleep(random.randint(2,6))
        jxx(json_data1)