from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

# stick : 방향으로 늘려 줌 N E W S 동서남북
# padx pady : 중간 글자 기준으로 가로 세로 값을 줌
btn_16 = Button(root, text='F16', padx=10, pady=10)
btn_17 = Button(root, text='F17', padx=10, pady=10)
btn_18 = Button(root, text='F18', padx=10, pady=10)
btn_19 = Button(root, text='F19', padx=10, pady=10)

btn_16.grid(row=0, column=0, sticky=N+E+W+S)
btn_17.grid(row=0, column=1, sticky=N+E+W+S)
btn_18.grid(row=0, column=2, sticky=N+E+W+S)
btn_19.grid(row=0, column=3, sticky=N+E+W+S)

btn_clear = Button(root, text='clear', padx=10, pady=10)
btn_5 = Button(root, text='=', padx=10, pady=10)
btn_6 = Button(root, text='/', padx=10, pady=10)
btn_plus = Button(root, text='*', padx=10, pady=10)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S)
btn_5.grid(row=1, column=1, sticky=N+E+W+S)
btn_6.grid(row=1, column=2, sticky=N+E+W+S)
btn_plus.grid(row=1, column=3, sticky=N+E+W+S)

btn_7 = Button(root, text='7', padx=10, pady=10)
btn_8 = Button(root, text='8', padx=10, pady=10)
btn_9 = Button(root, text='9', padx=10, pady=10)
btn_sub = Button(root, text='8', padx=10, pady=10)

btn_7.grid(row=2, column=0, sticky=N+E+W+S)
btn_8.grid(row=2, column=1, sticky=N+E+W+S)
btn_9.grid(row=2, column=2, sticky=N+E+W+S)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S)

btn_1 = Button(root, text='4', padx=10, pady=10)
btn_2 = Button(root, text='5', padx=10, pady=10)
btn_3 = Button(root, text='6', padx=10, pady=10)
btn_enter = Button(root, text='+', padx=10, pady=10)

btn_1.grid(row=3, column=0, sticky=N+E+W+S)
btn_2.grid(row=3, column=1, sticky=N+E+W+S)
btn_3.grid(row=3, column=2, sticky=N+E+W+S)
btn_enter.grid(row=3, column=3, sticky=N+E+W+S)

btn_1 = Button(root, text='1', padx=10, pady=10)
btn_2 = Button(root, text='2', padx=10, pady=10)
btn_3 = Button(root, text='3', padx=10, pady=10)
btn_enter = Button(root, text='enter', padx=10, pady=10)

btn_1.grid(row=4, column=0, sticky=N+E+W+S)
btn_2.grid(row=4, column=1, sticky=N+E+W+S)
btn_3.grid(row=4, column=2, sticky=N+E+W+S)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S) # rowspan : 현재 위치로 부터 아래쪽으로 합침

btn_0 = Button(root, text='0', padx=10, pady=10)
btn_point = Button(root, text='.', padx=10, pady=10)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S) # columspan : 현재 위치로부터 오른쪽으로 합침
btn_point.grid(row=5, column=2, sticky=N+E+W+S)



root.mainloop()