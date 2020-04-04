import requests
from bs4 import BeautifulSoup
import os
import time

i = 7792
alert = '삭제되었거나 존재하지 않는 게시물입니다.'
desktop = 'C:/Users/elder/Desktop/cris_saves'

while i > 0:
    url = f'https://cris.nih.go.kr/cris/search/search_result_st01_kren.jsp?seq={i}&ltype=&rtype='
    try:
        html = requests.get(url)
    except(e):
        print(f'{e} occurred. Sleeping...')
        time.sleep(10)
        continue
    soup = BeautifulSoup(html.text, 'html.parser')
    path = os.path.join(desktop, f'{i}.html')
    if alert in soup.get_text():
        print(f'{i} doesn\'t exist.')
        pass
    else:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(html.text)
            print(f'{i}.html created')
            time.sleep(1)
    i -= 1
