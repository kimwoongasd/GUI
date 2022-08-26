from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

# chbox에 int형으로 값을 저장한다
chvar = IntVar()
chbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chvar)

# chbox.select() # 자동 선택 처리
# chbox.deselect() # 선택 해제 처리
chbox.pack()

chvar2 = IntVar()
chbox2 = Checkbutton(root, text='오늘 하루 보지 않기', variable=chvar2)
chbox2.pack()

def btncmd():
    # 체크 면 1 체크 헤제 : 0
    print(chvar.get())
    print(chvar2.get())

btn = Button(root, text='버튼', command=btncmd)
btn.pack()


root.mainloop()