from PIL import ImageGrab
import time

# 5초 대기 : 사용자 설정 준비
time.sleep(5)

# 2초 간격으로 10개 이미지 저장
for i in range(1, 11):
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save(f'image{i}.png') # 파일로 저장
    time.sleep(2)