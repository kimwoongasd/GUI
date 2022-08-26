from tkinter import *
import tkinter.ttk as ttk

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

# 글 쓰기 가능 
values = [str(i) + '일' for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values= values)
combobox.pack()
combobox.set('카드 결제일')

# state='readonly' : 읽기 전용 변경 불가
readonly_combobox = ttk.Combobox(root, height=5, values= values, state='readonly')
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text='선택', command=btncmd)
btn.pack()


root.mainloop()