import random
import time

songs = ["a노래", "b노래", "c노래", "d노래"]
print(songs)

print(songs[3])

for A in songs:
    print(A)

print("노래 추천좀")
print("""
좋아요, 제가 열심히 분석해서
노래 한 곡 추천해 드릴게요""")

ai_song = random.choice(songs)

DDDD = ["두", "두", "두","둥"]

for num in DDDD:
    print(num)
    time.sleep(1) 

print(f"제 추천곡은 {ai_song}입니다")