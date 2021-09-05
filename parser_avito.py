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


# print(parse('https://auto.drom.ru/region61/lada/priora/', '42636762'))




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