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

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both')

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extend', height=15,yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임

save_frame = LabelFrame(root, text='저장경로')
save_frame.pack()

save_list = Listbox(save_frame, selectmode='extend', height=1)
save_list.pack(side='left')

btn_find = Button(save_frame, text='찾아보기')
btn_find.pack()

root.resizable(False, False)
root.mainloop()