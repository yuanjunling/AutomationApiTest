from tkinter import *
top=Tk()

def clicked():
    print('I was clicked')
# Label( text="I'm in the first window!").pack()
# second = Toplevel()
# Label(second,text="I'm in the first window!").pack()
# Button(text='按钮',command=clicked).pack()
for i in range(10):
    Button(text=i).pack()
mainloop()