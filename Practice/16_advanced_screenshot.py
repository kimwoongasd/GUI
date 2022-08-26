import keyboard
from PIL import ImageGrab
import time

def screenshot():
    cur = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save(f'img{cur}.png')

# f9 누르면 스크린샷 저장
keyboard.add_hotkey('F9', screenshot)

# esc 누르면 스크리샷 중지
keyboard.wait('esc')