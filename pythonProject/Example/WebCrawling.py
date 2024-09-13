from bs4 import BeautifulSoup
import urllib.request

Hollys_stores = list()

# for page in range(1, 51):
#     Hollys_url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="
#     print(Hollys_url)


# html = urllib.request.urlopen("https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=20&sido=&gugun=&store=")
# print(html)
#
# soup_hollys = BeautifulSoup(html, "html.parser")
# print(soup_hollys)


for page in range(1, 51):
    Hollys_url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store="
    print(Hollys_url)
    html = urllib.request.urlopen(Hollys_url)
    soup_hollys = BeautifulSoup(html, 'html.parser')
    tag_t_body = soup_hollys.find('tbody')

    for store in tag_t_body.find_all('tr'):
        if len(store) <= 3:
            break
        store_td = store.find_all('td')
        store_name = store_td[1].string
        store_sido = store_td[0].string
        store_address = store_td[3].string
        store_phone = store_td[5].string

        Hollys_stores.append([store_name] +
                             [store_sido] +
                             [store_address] +
                             [store_phone])


print(f'RESULT of Crawling : \r\n{Hollys_stores}')

# print(Hollys_stores[0])

import pandas as pd

Hollys_tbl = pd.DataFrame(data=Hollys_stores,
                          columns=('매장', '도시', '주소', '전화번호'))
Hollys_tbl.to_csv("./Hollys_table_EXCEL.csv",
                  encoding='cp949', mode='w', index=True)
Hollys_tbl.to_csv("./Hollys_table.csv",
                  encoding='utf-8', mode='w', index=True)