from fileinput import filename
from tkinter import *
import tkinter.messagebox as msgbox
import os

root = Tk()
root.title('제목 없음 - windows 메모장')
root.geometry('320x400')

# 나도코딩의 함수
# filename = 'mynote.txt'

# def opening():
#     if os.path.isfile(filename):
#         with open(filename, 'r', encoding='UTF-8') as file:
#             txt.delete('1.0', END)
#             txt.insert(END, file.read())
    
# def save():
#     with open(filename, 'w', encoding='UTF-8') as file:
#             file.write(txt.get('1.0', END))

# 열기 함수
def opening():
    try:
        f = open('mynote.txt', 'r', encoding='UTF-8')
        file = f.read()
        txt.delete('1.0', END)
        txt.insert(END, file)
        f.close()
        
    except:
        msgbox.showerror('에러', '파일을 찾을 수 없습니다.')
    
# 저장 함수
def save():
    file = open('mynote.txt', 'w', encoding='UTF-8')
    file.write(txt.get('1.0', END))
    file.close()


# 프로그램 종료 함수
def quit():
    root.quit()

menu = Menu(root)

# tearoff 줄 제거
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기(O)', command=opening)
menu_file.add_command(label='저장(S)', command=save)
menu_file.add_separator()
menu_file.add_command(label='끝내기(X)', command=quit)

menu.add_cascade(label='파일(F)', menu=menu_file)

menu.add_cascade(label='편집(E)')
menu.add_cascade(label='서식(O)')
menu.add_cascade(label='보기(V)')
menu.add_cascade(label='도움말(H)')

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# 텍스트
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill='both', expand=True)

# 텍스트와 스크롤바 맵핑
scrollbar.config(command=txt.yview)

# 화면에 보여주게 만들어 줌
root.config(menu=menu)
root.mainloop()
