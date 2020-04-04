from bs4 import BeautifulSoup
import glob
import pandas as pd
import time
import multiprocessing

d = {
    # 'summary_title': {
    #     'kr': '#printDiv > div > div.viw_tb > table > tbody > tr:nth-child(3) > td',
    #     'en': '#printDiv > div > div.viw_tb > table > tbody > tr:nth-child(4) > td'
    # },
    # 'study_title': {
    #     'kr': '#printDiv > div > div.viw_tb > table > tbody > tr:nth-child(5) > td',
    #     'en': '#printDiv > div > div.viw_tb > table > tbody > tr:nth-child(6) > td'
    #  },
    #  'cmte': {
    #      'kr': '#printDiv > div > div:nth-child(3) > div.viw_tb > table > tbody > tr:nth-child(4) > td',
    #      'en': '#printDiv > div > div:nth-child(3) > div.viw_tb > table > tbody > tr:nth-child(5) > td'
    #  },
    # 'p_invest': {
    #     'kr': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(2) > td',
    #     'en': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(3) > td'
    # },
    # 'p_position': {
    #     'kr': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(4) > td',
    #     'en': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(5) > td'
    # },
    # 'a_position': {
    #     'kr': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(12) > td',
    #     'en': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(13) > td'
    # },
    # 'i_name': {
    #     'kr': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(15) > td',
    #     'en': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(16) > td'
    # },
    # 'r_position': {
    #     'kr': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(20) > td',
    #     'en': '#printDiv > div > div:nth-child(4) > div.viw_tb > table > tbody > tr:nth-child(21) > td'
    # },
    # 's_name': {
    #     'kr': '#printDiv > div > div:nth-child(6) > div.viw_tb > table > tbody > tr:nth-child(2) > td',
    #     'en': '#printDiv > div > div:nth-child(6) > div.viw_tb > table > tbody > tr:nth-child(3) > td'
    # },
    # 'research_inst': {
    #     'kr': '#printDiv > div > div:nth-child(7) > div.viw_tb > table > tbody > tr:nth-child(2) > td',
    #     'en': '#printDiv > div > div:nth-child(7) > div.viw_tb > table > tbody > tr:nth-child(3) > td'
    # },
    #  'study_summary': {
    #      'kr': '#printDiv > div > div:nth-child(8) > div.viw_tb > table > tbody > tr:nth-child(1) > td',
    #      'en': '#printDiv > div > div:nth-child(8) > div.viw_tb > table > tbody > tr:nth-child(2) > td'
    #  },
    # 'observe': {
    #     'kr': '#printDiv > div > div:nth-child(9) > div.viw_tb > table > tbody > tr:nth-child(6) > td',
    #     'en': '#printDiv > div > div:nth-child(9) > div.viw_tb > table > tbody > tr:nth-child(7) > td'
    # },
    #  'detail': {
    #      'kr': '#printDiv > div > div:nth-child(9) > div.viw_tb > table > tbody > tr:nth-child(8) > td',
    #      'en': '#printDiv > div > div:nth-child(9) > div.viw_tb > table > tbody > tr:nth-child(9) > td'
    #  },
    # 'subjects': {
    #     'kr': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(1) > td',
    #     'en': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(2) > td'
    # },
    # 'subject_selection': {
    #     'kr': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(3) > td',
    #     'en': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(4) > td'
    # },
    # 'subject_standard': {
    #     'kr': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(11) > td',
    #     'en': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(12) > td'
    # },
    # 'subject_exclusion': {
    #     'kr': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(13) > td',
    #     'en': '#printDiv > div > div:nth-child(10) > div.viw_tb > table > tbody > tr:nth-child(14) > td'
    # },
    # 'evaluation_cate': {
    #     'kr': '#printDiv > div > div:nth-child(11) > div.viw_tb > table > tbody > tr:nth-child(3) > td',
    #     'en': '#printDiv > div > div:nth-child(11) > div.viw_tb > table > tbody > tr:nth-child(4) > td'
    # },
    # 'evaluation_time': {
    #     'kr': '#printDiv > div > div:nth-child(11) > div.viw_tb > table > tbody > tr:nth-child(5) > td',
    #     'en': '#printDiv > div > div:nth-child(11) > div.viw_tb > table > tbody > tr:nth-child(6) > td'
    # },
    # 'evaluation_item': {
    #     'kr': '#printDiv > div > div:nth-child(11) > div.viw_tb > table > tbody > tr:nth-child(8) > td',
    #     'en': '#printDiv > div > div:nth-child(11) > div.viw_tb > table > tbody > tr:nth-child(9) > td'
    # }
}

def parse_save(f):
    df = pd.DataFrame(columns = ['kr', 'en'])
    file_name = f.split('\\')[-1]
    with open(f, 'r', encoding = 'utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        for k, v in d.items():
            data = {
                'file_name': file_name
            }
            
            for lang, sel in v.items():
                parsed_data = soup.select(sel)
                if len(parsed_data) > 0:
                    data[lang] = parsed_data[0].text.strip().replace('\t', '')
            df = df.append(data, ignore_index=True)
        df.to_csv('C:/Users/elder/Desktop/my_csv.csv', mode='a', header=False, encoding='utf-8-sig')

def test(file):
    soup = BeautifulSoup(file, 'html.parser')
    txtct = soup.find_all('th', class_='txtct')
    for i in txtct:
        print(i.next_sibling.next_sibling.get_text())

# if __name__ == "__main__":
#     start_time = time.time()
#     pool = multiprocessing.Pool(14)
#     for file in glob.glob(r'C:\Users\elder\Desktop\cris_saves\*.html')[:1000]:
#         pool.apply_async(parse_save, [file])
#     pool.close()
#     pool.join()
#     print(f'elapsed: {time.time() - start_time}')

#add encoding for df.to_csv in 103. try utf-8 and then utf-8-sig <- idea) find out the difference
#study about multiprocessing

with open(r'C:\Users\elder\Desktop\cris_saves\10104.html', 'r', encoding = 'utf-8') as f:
    test(f)
    
