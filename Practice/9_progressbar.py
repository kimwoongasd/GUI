from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')


# mode='indeterminate' : 언제 끝날지 모르는 작업
# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
# progressbar.start(5)
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar2.start(5)
# progressbar2.pack()

p_var = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var)
progressbar3.pack()

def start():
    for i in range(1, 101):
        time.sleep(0.01)
        # progressbar의 값 설정
        p_var.set(i)
        # 업데이트 하지않으면 끝난 화면이 출력
        progressbar3.update()
        print(p_var.get())

btn2 = Button(root, text='시작', command=start)
btn2.pack()

def btncmd():
    # 중지
    # progressbar.stop()
    # progressbar2.stop()
    pass

btn = Button(root, text='중지', command=btncmd)
btn.pack()


root.mainloop()