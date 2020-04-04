from bs4 import BeautifulSoup
import glob
import pandas as pd
import time
import multiprocessing
import numpy as np


def parse_save(f):
    
    file_name = f.split('\\')[-1]
    print(f)
    with open(f, 'r', encoding = 'utf-8') as f:

        soup = BeautifulSoup(f, 'html.parser')
        txtct = soup.find_all('th', class_='txtct')
        data = {}

        data['file_name'] = []
        data['kr'] = []
        data['en'] = []
        
        for i in range(len(txtct))[0::2]:
            text_to_get = lambda x: txtct[x].next_sibling.next_sibling.get_text().replace('\t', '').strip()
            split_by_break = lambda x: len(x.split('\n'))

            korean = text_to_get(i)
            english = text_to_get(i+1)

            if split_by_break(korean) == split_by_break(english):
                for a in korean.split('\n'):
                    data['kr'].append(a)
                for a in english.split('\n'):
                    data['en'].append(a)

        for _ in range(len(data['kr'])):
            data['file_name'].append(file_name)

        df = pd.DataFrame(data, columns = ['file_name', 'kr', 'en'])
        df.drop_duplicates(inplace=True)
        df['kr'].replace('', np.nan, inplace=True)
        df['en'].replace('', np.nan, inplace=True)
        df.dropna(axis=0, how='any', inplace=True)
        df.reset_index(inplace=True, drop=True)
        df.to_csv('C:/Users/elder/Desktop/my_csv.csv', mode='a', header=False, encoding='utf-8-sig')

def test(file):
    soup = BeautifulSoup(file, 'html.parser')
    txtct = soup.find_all('th', class_='txtct')
    for i in txtct:
        if i.get_text() == '국문':
            print(i.next_sibling.next_sibling.get_text())

if __name__ == "__main__":
    start_time = time.time()
    pool = multiprocessing.Pool(14)
    for file in glob.glob(r'C:\Users\elder\Desktop\cris_saves\*.html'):
        pool.apply_async(parse_save, [file])
    pool.close()
    pool.join()
    print(f'elapsed: {time.time() - start_time}')


# parse_save(r'C:\Users\elder\Desktop\cris_saves\11127.html')
    
