import requests
from bs4 import BeautifulSoup
import random
import time

print("==================")
print("1. 멜론 top 100")
print("2. 멜론 top 50")
print("3. 멜론 top 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("==================")
# 멜론 차트 주소
url = "https://www.melon.com/chart/index.htm"

# 일반 웹브라우저처럼 보이도록 User-Agent 설정
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.66 Safari/537.36"
    )
}

# 1. GET 요청으로 HTML 가져오기
response = requests.get(url, headers=headers)

# 2. BeautifulSoup로 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 3. 'lst50'과 'lst100' 클래스가 붙은 tr 태그에서 곡 정보 찾기
#   - 멜론은 TOP 50을 lst50, 51~100위를 lst100 태그로 구분하기도 함.
songs = []

# 멜론 차트의 노래 제목과 아티스트를 찾습니다.
#lst50 #frm > div > table > tbody #lst50
for entry in soup.select('tr.lst50, tr.lst100'):  # 상위 50위 및 100위 목록
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 메뉴선택(입력) : 1
n = input("메뉴선택: ")
#print(f"당신이 입력한 값은? {n}")

# 만약 1을 입력하면
# 멜론 top 100 출력
# n = int(n) / n은 정수, 연산을 해야한다면
if n == "1":
    print("멜론 TOP100")
    # 4. 추출 결과 출력
    for i in range(100):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")



# 메뉴선택(입력) : 2
# 만약 2을 입력하면
# 멜론 top 50 출력
elif n == "2":
    print("멜론 TOP50")

elif n == "3":
    print("멜론 TOP10")

elif n == "4":
    print("AI 노래 추천")
    
    melon = random.choice(songs)
    random_rank, random_title, random_artist = melon
    print("오늘 멜론 Top 100 추천곡은")

    print(f"{random_rank}위 '{random_artist} - {random_title}' 입니다.") 
# 메뉴선택(입력) : 5
# 만약 5을 입력하면
# 가수 이름 검색
elif n == "5":
    print("가수 검색")
    artist = input("가수를 입력하세요: ")

# 5를 입력하면 가수이름을 입력할 입력창 필요
# 가수 입력 시 해당 가수 노래 리스트 출력

else:
    print("1~5까지 값을 입력하세요")
