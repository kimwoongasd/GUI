from tkinter import *
import tkinter.messagebox as msgbox

db = []

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

Label(root, text='메뉴를 선택해 주세요').pack(side='top')
Button(root, text='주문').pack(side='bottom')

# 외각 fill : 위아래로 채우기 
frame_burger = Frame(root, relief='solid', bd=1)
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈햄버거').pack()
Button(frame_burger, text='치킨햄버거').pack()

frame_drink = LabelFrame(root, text='음료')
frame_drink.pack(side='right', fill='both', expand=True)
Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop()