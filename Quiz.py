from tkinter import *

root = Tk()
root.title('제목 없음 - windows 메모장')
root.geometry('320x400')

# 프로그램 종료 함수
def quit():
    root.quit()

menu = Menu(root)

# tearoff 줄 제거
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기(O)')
menu_file.add_command(label='저장(S)')
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

# 화면에 보여주게 만들어 줌
root.config(menu=menu)
root.mainloop()
