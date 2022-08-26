from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

# 글 쓸수있는 텍스트 생성
txt = Text(root, width=30, height=5)
txt.pack()

# 기본 값등 미리 넣기 가능
# 엔터기능 가능
txt.insert(END, '글자를 입력하세요')

# 엔터기능 불가능
e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력하세요')

def btncmd():
    # 1 : 첫번쨰 라인, 0 : 0번쨰 column 위치
    # 값 가져오기
    print(txt.get('1.0', END))
    print(e.get())
    
    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(root, text='버튼', command=btncmd)
btn.pack()


root.mainloop()