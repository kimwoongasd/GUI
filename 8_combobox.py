from tkinter import *
import tkinter.ttk as ttk

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')


values = [str(i) + '일' for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values= values)
combobox.pack()

def btncmd():
    pass

btn = Button(root, text='주문', command=btncmd)
btn.pack()


root.mainloop()