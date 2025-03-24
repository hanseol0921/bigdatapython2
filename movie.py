import requests

# 🔹 여기에 발급받은 API 키 입력
API_KEY = "ef8ad0432857b990802534d21af9585b"  

# 🔹 조회할 날짜 설정 (YYYYMMDD 형식)
DATE = "20240323"  # 예시로 2024년 3월 23일 데이터 조회

# 🔹 KOBIS API 요청 URL (일별 박스오피스 조회)
URL = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={API_KEY}&targetDt={DATE}"

response = requests.get(URL)

# 🔹 상태 코드 확인 (200이면 정상)
print("응답 상태 코드:", response.status_code)

# 🔹 데이터 확인
try:
    data = response.json()
    if "boxOfficeResult" in data:
        print(f"🎬 {DATE}일자 일별 박스오피스 목록:")
        for movie in data["boxOfficeResult"]["dailyBoxOfficeList"]:
            title = movie["movieNm"]
            
            # 관객수를 정수로 변환 (숫자가 아닌 경우 기본값 0)
            try:
                audience = int(movie["audiAcc"])  # 관객 수를 정수로 변환
            except ValueError:
                audience = 0  # 변환 실패 시 0으로 설정

            print(f"🎥 영화: {title} | 관객수: {audience:,}명")
    else:
        print("❌ 데이터가 없습니다.")
except Exception as e:
    print(f"❌ 오류 발생: {e}")