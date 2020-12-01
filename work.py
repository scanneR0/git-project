from tkinter import *

def button_click ():
    print('Ошибка')

root = Tk ()

root['bg'] = '#fafafa'
root.title('Сумма и произведение')
root.wm_attributes('-alpha', 1)
root.geometry('300x250')   
root.resizable(False, False) 

canvas = Canvas(root, height=300, width=250)
canvas.pack

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Введите трехзначное число', bg="white", font=40)
title.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

btn=Button(frame, text='Вывод', command=button_click)
btn.pack()


root.mainloop() 