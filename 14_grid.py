from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

btn_16 = Button(root, text='F16')
btn_17 = Button(root, text='F17')
btn_18 = Button(root, text='F18')
btn_19 = Button(root, text='F19')
btn_16.grid(row=0, column=0)
btn_17.grid(row=0, column=1)
btn_18.grid(row=0, column=2)
btn_19.grid(row=0, column=3)

btn_clear = Button(root, text='clear')
btn_5 = Button(root, text='=')
btn_6 = Button(root, text='/')
btn_plus = Button(root, text='*')
btn_clear.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_plus.grid(row=1, column=3)

btn_7 = Button(root, text='7')
btn_8 = Button(root, text='8')
btn_9 = Button(root, text='9')
btn_sub = Button(root, text='8')
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

btn_1 = Button(root, text='4')
btn_2 = Button(root, text='5')
btn_3 = Button(root, text='6')
btn_enter = Button(root, text='+')
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_enter.grid(row=3, column=3)

btn_1 = Button(root, text='1')
btn_2 = Button(root, text='2')
btn_3 = Button(root, text='3')
btn_enter = Button(root, text='enter')
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)


btn_enter.grid(row=4, column=3, rowspan=2) # rowspan : 현재 위치로 부터 아래쪽으로 합침
btn_0 = Button(root, text='0')
btn_point = Button(root, text='.')
btn_0.grid(row=5, column=0, columnspan=2) # columspan : 현재 위치로부터 오른쪽으로 합침
btn_point.grid(row=5, column=2)



root.mainloop()