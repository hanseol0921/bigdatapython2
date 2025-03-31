import requests
from bs4 import BeautifulSoup

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

print(response)
