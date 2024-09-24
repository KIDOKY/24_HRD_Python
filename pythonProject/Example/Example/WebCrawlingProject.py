from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# 저장할 데이터를 담을 리스트
Yestwo_stores = []

# 크롤링할 페이지 범위 설정
for page in range(1, 11):
    # URL 설정
    Yestwo_url = f"https://www.yes24.com/24/Category/Display/001001046003?PageNumber={page}"
    print(Yestwo_url)

    # 페이지 요청
    html = urllib.request.urlopen(Yestwo_url)
    soup_Yestwo = BeautifulSoup(html, 'html.parser')

    # 데이터가 있는 영역을 찾기
    main_content = soup_Yestwo.find('div', {'class': 'basicList_info_area'})

    if main_content is None:
        print(f"No content found on page {page}")
        continue

    # 데이터 추출
    for item in main_content.find_all('div', {'class': 'basicList_info'}):
        try:
            book_name = item.find('div', {'class': 'goods_name'}).find('a').text.strip()

            # 저자 정보
            author_info = item.find('span', {'class': 'goods_auth'}).text.strip() if item.find('span', {
                'class': 'goods_auth'}) else 'N/A'

            # 출판사
            publisher = item.find('span', {'class': 'goods_pub'}).text.strip() if item.find('span', {
                'class': 'goods_pub'}) else 'N/A'

            # 평점
            rating = item.find('span', {'class': 'gd_rating'}).find('em', {'class': 'yes_b'}).text.strip() if item.find(
                'span', {'class': 'gd_rating'}) else 'N/A'

            # 회원리뷰수
            review_count = item.find('span', {'class': 'gd_reviewCount'}).find('em').text.strip() if item.find('span', {
                'class': 'gd_reviewCount'}) else 'N/A'
        except AttributeError:
            continue  # 데이터가 없는 항목은 건너뜁니다.

        Yestwo_stores.append([book_name, author_info, publisher, rating, review_count])

print(f"RESULT of Crawling : \r\n{Yestwo_stores}")

# 데이터프레임 생성
Yestwo_tbl = pd.DataFrame(data=Yestwo_stores, columns=['도서명', '저자 정보', '출판사', '평점', '회원리뷰수'])

# CSV 파일로 저장
Yestwo_tbl.to_csv("./Yestwo_table_EXCEL.csv", encoding='cp949', mode='w', index=True)
Yestwo_tbl.to_csv("./Yestwo_table.csv", encoding='utf-8', mode='w', index=True)
