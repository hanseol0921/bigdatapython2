import csv

data = [
    ['순위', '제목 '가수,
    ['1','1노래, '1가수'],
    ['2', 2노래, '2가수'],
    ['3', 3노래, '3가수']
]

file_path = 'music.cvs'
try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    
    # 여러 행을 한 번에 쓰기
    csv_writer.writerows(data)