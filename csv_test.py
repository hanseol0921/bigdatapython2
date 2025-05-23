import csv

data_to_write = [
    ['순위', '제목', '가수'],
    [1, '1노래', '1가수'],
    [2, '2노래', '2가수'],
    [3, '3노래', '3가수']
]
file_path = 'music.csv'
try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)

    print(f"'{file_path}' 파일이 성공적으로 생성되었습니다.")

except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")



    def melon_csv(f):
        print(f)
    song_list = melon_chart(100)

    try:
        with open("melon_chart.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["순위", "제목", "아티스트"])
            writer.writerows(song_list)

        print(f"'{'melon_chart.csv'}' 파일이 성공적으로 생성되었습니다.")

    except Exception as e:
        print(f"파일 쓰기 중 오류 발생: {e}")