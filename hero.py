from tkinter import*

win = Tk()
win.title('단위 변환기')


def conversion(event):
  cm = int(entry.get())
  inch = cm*0.39
  lbl3['text'] = '%.2f' % inch

lbl1 = Label(win, text = 'cm입력 :')
entry = Entry(win)
entry.bind('<Return>', conversion)
lbl2 = Label(win,text = 'inch :')
lbl3 = Label(win,text ='0.00')

lbl1.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)
lbl2.grid(row = 1, column = 0)
lbl3.grid(row = 1,column =1)
