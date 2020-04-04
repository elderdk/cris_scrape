from bs4 import BeautifulSoup
import glob
import pandas as pd
import time
import multiprocessing


def parse_save(f):
    df = pd.DataFrame(columns = ['file_name', 'kr', 'en'])
    file_name = f.split('\\')[-1]
    print(f)
    with open(f, 'r', encoding = 'utf-8') as f:

        soup = BeautifulSoup(f, 'html.parser')
        txtct = soup.find_all('th', class_='txtct')
        data = {}
        
        for i in txtct:
            text_to_get = i.next_sibling.next_sibling.get_text().replace('\t', '').strip()
            data['file_name'] = file_name
            if i.get_text() == '국문':
                data['kr'] = text_to_get
            if i.get_text() == '영문':
                data['en'] = text_to_get
            if 'kr' in data.keys() and 'en' in data.keys():
                df = df.append(data, ignore_index=True)
                data = {}

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
    for file in glob.glob(r'C:\Users\elder\Desktop\cris_saves\10123.html')[0]:
        pool.apply_async(parse_save, [file])
    pool.close()
    pool.join()
    print(f'elapsed: {time.time() - start_time}')

#add encoding for df.to_csv in 103. try utf-8 and then utf-8-sig <- idea) find out the difference
#study about multiprocessing

# parse_save(r'C:\Users\elder\Desktop\cris_saves\10104.html')
    
