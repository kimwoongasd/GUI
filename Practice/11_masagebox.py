from tkinter import *
import tkinter.messagebox as msgbox

db = []

root = Tk()
# 타이틀 이름
root.title('Images GUI')
# 창 크기 가로 * 세로
root.geometry('640x480')

# 기차 예매 시스템 가정
def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료')
    
def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다')
    
def error():
    msgbox.showerror('에러', '결제 오류가 발생했습니다.')
    
def okcancle():
    msgbox.askokcancel('확인 / 취소', '해당 좌석은 유아동반석입니다. 예매하시겠습니까?')

def retrtcancle():
    msgbox.askretrycancel('재시도 / 취소', '일시적 오류입니다. 다시 시도하겠습니까?')

def yesno():
    msgbox.askyesno('예 / 아니오', '해당 좌석은 역방향입니다. 예매하시겠습니까?')

def yesnocancle():
    response = msgbox.askyesnocancel(title=None, message='예매 내역이 저장되지 않았습니다. \n예매 하시겠습니까?')
    # 예 : 저장 후 종료
    # 아니오 : 저장 하지않고 종료
    # 프로그램 종료 취소(현재 화면에서 계속 작업)
    print(response)
    if response == 1:
        db.append(response)
        root.quit()
    
    elif response == 0:
        root.quit()
        

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()
Button(root, command=okcancle, text='확인취소').pack()
Button(root, command=retrtcancle, text='재시도 취소').pack()
Button(root, command=yesno, text='예 / 아니오').pack()
Button(root, command=yesnocancle, text='예 / 아니오 / 취소').pack()


root.mainloop()