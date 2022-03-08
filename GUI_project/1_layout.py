from tkinter import *

root = Tk()
root.title('GUI Image')


# 파일 프레임 (파일 추가, 선택삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,text='파일 추가')
btn_sel_del = Button(file_frame, padx=5, pady=5, width=12,text='선택 삭제')

btn_add_file.pack(side='left')
btn_sel_del.pack(side='right')

root.resizable(False, False)
root.mainloop()