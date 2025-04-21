import func


print("==========================")
print("1. 멜론 TOP100")
print("2. 멜론 TOP50")
print("3. 멜론 TOP10")
print("4. 노래 추천 기능")
print("5. TOP100 가수 검색")
print("6. 파일에 저장 (멜론TOP100)")
print("==========================")

n = input("메뉴를 입력하세요: ")

if n == "1":
    func.m100("[멜론 TOP100]")
elif n == "2":
    func.m50("[멜론 TOP50]")
elif n == "3":
    func.m10("[멜론 TOP10]")
elif n == "4":
    func.m_random("[노래 추천 기능]")
elif n == "5":
    func.m_artist("[TOP100 가수 검색]")
elif n == "6":
    func.melon_csv("[멜론 TOP100을 파일에 저장합니다.]")


else:
    print("1~56까지의 수를 입력해 주세요")

#func.m000("[멜론내맘대로출력]", 5)
