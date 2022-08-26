from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

label1 = Label(root, text='메뉴를 선택하세요')
label1.pack()

bugger_var = IntVar()
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=bugger_var)
btn_burger2 = Radiobutton(root, text='치즈햄버거', value=2, variable=bugger_var)
btn_burger3 = Radiobutton(root, text='치킨햄버거', value=3, variable=bugger_var)
btn_burger1.select()
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text='음료를 선택하세요')
label2.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)
btn_drink1.select()
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    # 버거버튼 value 값이 출력
    print(bugger_var.get())
    print(drink_var.get())

btn = Button(root, text='주문', command=btncmd)
btn.pack()


root.mainloop()