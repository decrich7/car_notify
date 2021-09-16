# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time


def parse(url, id):
    fake_ua = UserAgent()
    headers = {
        'user-agent': fake_ua.random
    }
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('a', class_='css-1psewqh ewrty961')
    car_info = []
    for item in items:
        link_objv = str(item.get('href'))
        req = requests.get(url=link_objv, headers=headers)
        soup2 = BeautifulSoup(req.content, 'lxml')
        if id == link_objv:
            return car_info
        else:
            price_new = str(soup2.find('div', class_='css-1003rx0 e162wx9x0').text)
            price = []
            price_final = []
            count = 1
            for i in price_new:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    price.append(str(i))
            for ineg in price:
                count += 1
                if len(price) == 7:
                    if count == 3 or count == 6:
                        price_final.append(' ')
                elif len(price) == 6:
                    if count == 5 or count == 8:
                        price_final.append(' ')
                elif len(price) == 5:
                    if count == 1 or count == 4:
                        price_final.append(' ')
                price_final.append(ineg)
            dict_params = {}
            list1 = [str(i.find('th').text) for i in soup2.find_all('tr', class_='css-11ylakv ezjvm5n0')]
            list2 = [str(i.find('td').text.replace('\xa0', ' ')) for i in
                     soup2.find_all('tr', class_='css-11ylakv ezjvm5n0')]
            for i in range(len(list1)):
                dict_params[list1[i]] = list2[i]

            car_info.append(
                {
                    'link': link_objv,
                    'picture': str(soup2.find('img', class_='css-1mnj4qi evrha4s0').get('src')),
                    'price': ''.join(price_final),
                    'params': dict_params,
                    'title': soup2.find('h1', class_='css-1rmdgdb e18vbajn0').text
                }
            )
    return car_info

# r = requests.get('https://webanetlabs.net/publ/24')
# soup = BeautifulSoup(r.text, 'lxml')
# proxi = soup.find('div', class_='eMessage').find('p').text.split('\n')
# print(proxi)
# proxy = {'http': proxi[0]}
# print(requests.get('https://wtfismyip.com/text', proxies=proxy).text)
# start = time.time()
# def parse(url, id):
#     # r = requests.get('https://webanetlabs.net/publ/24')
#     # soup = BeautifulSoup(r.text, 'lxml')
#     # proxi = soup.find('div', class_='eMessage').find('p').text.split('\n')
#     # print(proxi)
#     proxi = ['85.648.173.10:7528', '94.1536.1434.228:3128', '212.2240.15.15:3128', '156.54.2122.62:3128', '70.37.16425.170:3128']
#     proxy = {'http': proxi[0]}
#
#     fake_ua = UserAgent()
#     headers = {
#         'user-agent': fake_ua.random
#     }
#     r = requests.get(url=url, headers=headers, proxies=proxy)
#     soup = BeautifulSoup(r.text, 'lxml')
#     items = soup.find_all('a', class_='css-1psewqh ewrty961')
#     car_info = []
#     for item in items:
#         link_objv = str(item.get('href'))
#         req = requests.get(url=link_objv, headers=headers, proxies=proxy)
#         soup2 = BeautifulSoup(req.content, 'lxml')
#         if id == link_objv:
#             return car_info
#         else:
#             price_new = str(soup2.find('div', class_='css-1003rx0 e162wx9x0').text)
#             price = []
#             price_final = []
#             count = 1
#             for i in price_new:
#                 if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                     price.append(str(i))
#             for ineg in price:
#                 count += 1
#                 if len(price) == 7:
#                     if count == 3 or count == 6:
#                         price_final.append(' ')
#                 elif len(price) == 6:
#                     if count == 5 or count == 8:
#                         price_final.append(' ')
#                 elif len(price) == 5:
#                     if count == 1 or count == 4:
#                         price_final.append(' ')
#                 price_final.append(ineg)
#             dict_params = {}
#             list1 = [str(i.find('th').text) for i in soup2.find_all('tr', class_='css-11ylakv ezjvm5n0')]
#             list2 = [str(i.find('td').text.replace('\xa0', ' ')) for i in
#                      soup2.find_all('tr', class_='css-11ylakv ezjvm5n0')]
#             for i in range(len(list1)):
#                 dict_params[list1[i]] = list2[i]
#
#             car_info.append(
#                 {
#                     'link': link_objv,
#                     'picture': str(soup2.find('img', class_='css-1mnj4qi evrha4s0').get('src')),
#                     'price': ''.join(price_final),
#                     'params': dict_params,
#                     'title': soup2.find('h1', class_='css-1rmdgdb e18vbajn0').text
#                 }
#             )
#     return car_info
#
# print(parse('https://auto.drom.ru/kia/rio/', 'https://novorossiysk.drom.ru/kia/rio/43898932.html'))
#
# print(time.time()-start)


# import asyncio
# import time
# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# car_info = []
# async def get_page_data(url):
#     global car_info
#     fake_ua = UserAgent()
#     headers = {
#         'user-agent': fake_ua.random
#     }
#     link_objv = str(url.get('href'))
#     req = requests.get(url=link_objv, headers=headers)
#     soup2 = BeautifulSoup(req.content, 'lxml')
#     price_new = str(soup2.find('div', class_='css-1003rx0 e162wx9x0').text)
#     price = []
#     price_final = []
#     count = 1
#     for i in price_new:
#         if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             price.append(str(i))
#     for ineg in price:
#         count += 1
#         if len(price) == 7:
#             if count == 3 or count == 6:
#                 price_final.append(' ')
#         elif len(price) == 6:
#             if count == 5 or count == 8:
#                 price_final.append(' ')
#         elif len(price) == 5:
#             if count == 1 or count == 4:
#                 price_final.append(' ')
#         price_final.append(ineg)
#     dict_params = {}
#     list1 = [str(i.find('th').text) for i in soup2.find_all('tr', class_='css-11ylakv ezjvm5n0')]
#     list2 = [str(i.find('td').text.replace('\xa0', ' ')) for i in
#              soup2.find_all('tr', class_='css-11ylakv ezjvm5n0')]
#     for i in range(len(list1)):
#         dict_params[list1[i]] = list2[i]
#
#     car_info.append(
#         {
#             'link': link_objv,
#             'picture': str(soup2.find('img', class_='css-1mnj4qi evrha4s0').get('src')),
#             'price': ''.join(price_final),
#             'params': dict_params,
#             'title': soup2.find('h1', class_='css-1rmdgdb e18vbajn0').text
#         }
#     )
#
#
# async def get_url(url, url_id):
#     fake_ua = UserAgent()
#     headers = {
#         'user-agent': fake_ua.random
#     }
#     # async with aiohttp.ClientSession() as session:
#     #     response = await session.get(url='https://auto.drom.ru/region61/lada/priora/', headers=headers)
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'lxml')
#     items = soup.find_all('a', class_='css-1psewqh ewrty961')
#     tasks = []
#
#     for url in items:
#         if url.get('href') == url_id:
#             break
#         task = asyncio.create_task(get_page_data(url))
#         tasks.append(task)
#
#     await asyncio.gather(*tasks)


# def main(url, url_id):
#     asyncio.run(get_url(url, url_id))
#
#     return car_info


# get_url('https://auto.drom.ru/lada/priora/', 'https://lipetsk.drom.ru/lada/priora/43885346.html')
# #
# #
# print(car_info)