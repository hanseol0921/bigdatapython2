import requests
import json

# KOBIS 오픈 API - 일별 박스오피스 요청 URL 예시
# 자세한 내용은 KOBIS Open API 개발가이드 참고
# 실제 사용 시, 아래 YOUR_KEY를 본인의 발급받은 키 값으로 변경하세요

kobis_key = "YOUR_KEY"
search_date = "20230101"  # 조회할 날짜 (YYYYMMDD)
url = (
    "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    f"?key={kobis_key}&targetDt={search_date}"
)

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    box_office_result = data.get("boxOfficeResult", {})
    daily_box_office_list = box_office_result.get("dailyBoxOfficeList", [])

    for movie_info in daily_box_office_list:
        movie_name = movie_info.get("movieNm")
        audi_acc = movie_info.get("audiAcc")  # 누적관객수
        # "명탐정 코난" 제목 및 변형 가능성을 고려해 체크
        if "명탐정 코난" in movie_name:
            print(f"영화제목: {movie_name}, 누적 관객 수: {audi_acc}")
else:
    print("KOBIS API 요청 실패, 상태코드:", response.status_code)

    import requests
from bs4 import BeautifulSoup
import time

search_keyword = "名探偵コナン"

# 예시 URL (Eiga.com 검색 결과 페이지) 
# 실제 검색 페이지 URL은 변동 가능성이 큽니다.
base_url = "https://eiga.com/search/"
params = {
    "q": search_keyword,
    "tb": "movie"   # 영화 검색 탭 (실제와 다를 수 있음)
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

response = requests.get(base_url, params=params, headers=headers)
time.sleep(2)  # 잠시 대기

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # 예: 검색 결과 목록이 들어있는 특정 클래스 selector
    # (실제 사이트 HTML 구조 파악 필요)
    movie_list = soup.select(".m_unit h3 a")

    for link in movie_list:
        title = link.text.strip()
        detail_url = link.get("href")

        # 여기서는 영화 상세 페이지로 들어가 관객수·흥행수익 데이터가 있는지 추가 파싱
        if detail_url.startswith("/"):
            detail_url = "https://eiga.com" + detail_url
        
        detail_resp = requests.get(detail_url, headers=headers)
        if detail_resp.status_code == 200:
            detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
            # 상세 페이지에서 관객 수나 흥행 수익 표시되는 영역을 찾아 파싱
            # 예) 어떤 클래스나 태그에 흥행·관객 관련 문구가 있을 수 있음
            #     실제 예시가 없으므로 가상의 코드
            box_info = detail_soup.select_one(".box_office_data")
            if box_info:
                print(f"영화제목: {title}")
                print("흥행/관객정보:", box_info.text.strip())
                print("-" * 50)
else:
    print("Eiga.com 요청 실패, 상태코드:", response.status_code)
    