from tkinter import *

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

# extended : 여러개 선택 가능 single : 1개만 선택
# height = 숫자 : 나타내는 갯수
listbox = Listbox(root, selectmode='extended', height=0)
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(END)
    
    #갯수 확인
    #print(listbox.size())
    
    # 항목 확인
    # 시작 인덱스 부터 끝 인덱스 까지
    #print(listbox.get(0, 2))
    
    # 선택 항목 확인
    # 인덱스 값으로 나옴
    print(listbox.curselection())

btn = Button(root, text='버튼', command=btncmd)
btn.pack()


root.mainloop()