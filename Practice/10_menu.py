from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

def creat_new_file():
    print('새 파일을 만듭니다')

menu = Menu(root)
# file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='새 파일', command=creat_new_file)
menu_file.add_command(label='새 창')
menu_file.add_separator() # 구분자
menu_file.add_command(label='파일 열기')
menu_file.add_separator()
# state='disable' : 비활성화
menu_file.add_command(label='저장', state='disable')
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)

menu.add_cascade(label='파일(F)', menu=menu_file)

# 편집 메뉴
menu.add_cascade(label='편집(E)')

#언어 선택 메뉴 추가
# radiobox 사용
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='한글')
menu_lang.add_radiobutton(label='English')
menu_lang.add_radiobutton(label='日本語')

menu.add_cascade(label='언어', menu=menu_lang)

# checkbuyyon로 메뉴 추가
menu_check = Menu(menu, tearoff=0)
menu_check.add_checkbutton(label='미니맵 표시')
menu_check.add_checkbutton(label='이동 결로 표시')
menu_check.add_checkbutton(label='공백 랜더링')
menu_check.add_checkbutton(label='제어 문자 랜더링')

menu.add_cascade(label='보기', menu=menu_check)

root.config(menu=menu)
root.mainloop()