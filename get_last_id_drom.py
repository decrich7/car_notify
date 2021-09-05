# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent




def get_id(url):
    fake_ua = UserAgent()
    headers = {
        'user-agent': fake_ua.random
    }
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    url_id = soup.find('a', class_='css-1psewqh ewrty961').get('href')
    return url_id


