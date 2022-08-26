from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')

label1 = Label(root, text='인녕하세요')
label1.pack()

photo = PhotoImage(file='img.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    # 레이블 변경
    label1.config(text='또 만나요')
    
    global photo2
    # 전역변수로 선언하지 않으면 사진 갱신이 되지않음
    photo2 = PhotoImage(file='img2.png')
    label2.config(image=photo2)

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop()