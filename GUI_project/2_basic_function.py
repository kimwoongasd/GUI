from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

root = Tk()
root.title('GUI Image')

# 파일 추가
def add_file():
    filenames = filedialog.askopenfilenames(initialdir='c:/', title='파일추가', filetypes=(('png files','*.png'), ('jpg files','*.jpg'), ('bmp files', '*.bmp'), ('모든 파일', '*.*')))
    
    for filename in filenames:
        list_file.insert(END, filename)
        
# 파일 선택 삭제
def del_file():
    files = list_file.curselection()
    for index in files[::-1]:
        list_file.delete(index)
    
# 파일 프레임 (파일 추가, 선택삭제)
file_frame = Frame(root)
file_frame.pack(fill='both', expand=True, padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일 추가', command=add_file)
btn_sel_del = Button(file_frame, padx=5, pady=5, width=12, text='선택 삭제', command=del_file)

btn_add_file.pack(side='left')
btn_sel_del.pack(side='right')

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15,yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임

path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill='both', expand=True, padx=5, pady=5)

save_list = Entry(path_frame)
save_list.pack(side='left', fill='x', expand=True, ipady= 4, padx=5, pady=5)

btn_path = Button(path_frame, text='찾아보기', width=10)
btn_path.pack(side='right', padx=5, pady=5)

# 옵션 프레임

option_frame = LabelFrame(root, text='옵션')
option_frame.pack(padx=5, pady=5)

# 가로 넓이
# 가로 넓이 레이블
width_labal = Label(option_frame, text='가로 넓이', padx=10)
width_labal.pack(side='left', padx=5, pady=5)

# 가로 넓이 콤보박스
width_values = ['원본유지', '1024', '800', '640']
width_cbbox = ttk.Combobox(option_frame, values=width_values, state='readonly', width=10)
width_cbbox.current(0)
width_cbbox.pack(side='left', padx=5, pady=5)

# 간격
# 간격 레이블
interval_labal = Label(option_frame, text='간격', padx=10)
interval_labal.pack(side='left', padx=5, pady=5)

# 간격 콤보박스
interval_values = ['없음', '좁게', '넓게', '보통']
interval_cbbox = ttk.Combobox(option_frame, values=interval_values, state='readonly', width=10)
interval_cbbox.current(0)
interval_cbbox.pack(side='left', padx=5, pady=5)

# 포멧
# 포멧 레이블
format_label = Label(option_frame, text='포멧', padx=10)
format_label.pack(side='left', padx=5, pady=5)

# 포멧 콤보박스
format_values = ['PNG', 'JPG', 'BMP']
format_cbbox = ttk.Combobox(option_frame, values=format_values, state='readonly', width=10)
format_cbbox.current(0)
format_cbbox.pack(side='left', padx=5, pady=5)

# 진행상황 프레임
progress_frame = LabelFrame(root, text='진행상황')
progress_frame.pack(fill='x', expand=True, padx=5, pady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progressbar.pack(fill='x', padx=5, pady=5)

# 시작 닫기 버튼
run_frame = Frame(root)
run_frame.pack(fill='x', padx=5, pady=5)

btn_close = Button(run_frame, text='닫기', width=10, height=2, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)
btn_start = Button(run_frame, text='시작', width=10, height=2)
btn_start.pack(side='right', padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
