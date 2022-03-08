from msilib.schema import ComboBox
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('GUI Image')


# 파일 프레임 (파일 추가, 선택삭제)
file_frame = Frame(root)
file_frame.pack(fill='both', expand=True)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일 추가')
btn_sel_del = Button(file_frame, padx=5, pady=5, width=12, text='선택 삭제')

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

path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill='both', expand=True)

save_list = Entry(path_frame)
save_list.pack(side='left', fill='x', expand=True, ipady= 4)

btn_path = Button(path_frame, text='찾아보기', width=10)
btn_path.pack(side='right')

# 옵션 프레임

option_frame = LabelFrame(root, text='옵션')
option_frame.pack()

# 가로 넓이
# 가로 넓이 레이블
width_labal = Label(option_frame, text='가로 넓이', padx=10)
width_labal.grid(row=0, column=0)

# 가로 넓이 콤보박스
width_values = ['원본유지', '1024', '800', '640']
width_cbbox = ttk.Combobox(option_frame, values=width_values, state='readonly', width=10)
width_cbbox.current(0)
width_cbbox.grid(row=0, column=1)

# 간격
# 간격 레이블
interval_labal = Label(option_frame, text='간격', padx=10)
interval_labal.grid(row=0, column=2)

# 간격 콤보박스
interval_values = ['없음', '좁게', '넓게', '보통']
interval_cbbox = ttk.Combobox(option_frame, values=interval_values, state='readonly', width=10)
interval_cbbox.current(0)
interval_cbbox.grid(row=0, column=3)

# 포멧
# 포멧 레이블
format_label = Label(option_frame, text='포멧', padx=10)
format_label.grid(row=0, column=4)

# 포멧 콤보박스
format_values = ['PNG', 'JPG', 'BMP']
format_cbbox = ttk.Combobox(option_frame, values=format_values, state='readonly', width=10)
format_cbbox.current(0)
format_cbbox.grid(row=0, column=5)

root.resizable(False, False)
root.mainloop()