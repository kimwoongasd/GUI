from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title('GUI Image')

# 파일 추가
def add_file():
    # initialdir : 처음 시작 경로
    filenames = filedialog.askopenfilenames(initialdir='c:/', title='파일추가', filetypes=(('png files','*.png'), ('jpg files','*.jpg'), ('bmp files', '*.bmp'), ('모든 파일', '*.*')))
    
    for filename in filenames:
        list_file.insert(END, filename)
        
# 파일 선택 삭제
def del_file():
    files = list_file.curselection()
    for index in files[::-1]:
        list_file.delete(index)

# 폴더 저장 경로        
def save_path():
    save_list.delete(0, END)
    s_path = filedialog.askdirectory()
    save_list.insert(END, s_path)

def merge_image():
    #print(list_file.get(0, END)) # 모든 파일 목록 가져오기
    images = [Image.open(x) for x in list_file.get(0, END)]
    # size : size[0] : width,  size[1] : height
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]
    
    # zip을 사용할 경우
    #widths, heights = zip(*(x.size for x in images))
    
    # 최대 넓이와 높이 총합 구하기
    max_width, total_height = max(widths), sum(heights)
    
    # # 이미지를 합칠 스케치북
    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 흰색
    y_offset = 0 # y 위치
        
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1] # 높이 값 만큼 더함
        p_var.set(((idx + 1) / len(images)) * 100)
        progressbar.update()
        
    
    dest_path = os.path.join(save_list.get(), 'nado_photo.jpg') # 저장 경로
    result_img.save(dest_path) # 저장
    msgbox.showinfo('알림', '작업이 완료되었습니다.')
    
    # 완료 후 초기화
    list_file.delete(0, END)
    save_list.delete(0, END)
    p_var.set(0)
    width_cbbox.current(0)
    interval_cbbox.current(0)
    format_cbbox.current(0)
    
# 시작
def start():
    # 각 옵셥값 확인
    print('가로 넓이 :', width_cbbox.get())
    print('간격 :', interval_cbbox.get())
    print('포멧 :', format_cbbox.get())
    
    # 파일 추가 안했을 경우
    if list_file.size() == 0:
        msgbox.showwarning('경고', '파일을 추가해 주세요')
        return
    
    # 저장경로 입력하지 않은 경우
    if len(save_list.get()) == 0:
        msgbox.showwarning('경고', '저정경로를 설정해 주세요')
        return
    
    merge_image()
    
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

btn_path = Button(path_frame, text='찾아보기', width=10, command=save_path)
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
btn_start = Button(run_frame, text='시작', width=10, height=2, command=start)
btn_start.pack(side='right', padx=5, pady=5)


root.resizable(False, False)
root.mainloop()
