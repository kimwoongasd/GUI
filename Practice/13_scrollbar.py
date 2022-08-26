from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill = 'y')


# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()