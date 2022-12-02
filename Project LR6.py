import tkinter as tk
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Калькулятор ИМТ")
win.geometry('400x300')
win.resizable(0, 0)

fr1 =  Frame(
    win,
    padx=10,
    pady=10
)
fr1.pack(expand=True)

height_lb = Label(
    fr1,
    text="Введите свой рост(в см) "
)
height_lb.grid(row=3, column=1)

width_lb = Label(
    fr1,
    text="Введите свой вес(в кг) "
)
width_lb.grid(row=4, column=1)


heig_tf = Entry(
    fr1,
)
heig_tf.grid(row=3,column=2)

weigh_tf = Entry(
    fr1,
)
weigh_tf.grid(row=4, column=2, pady=5)

result = Label(
    fr1,
)
result.grid(row=5, column=1)
result.config(text="Тут результат ")

doc = Toplevel(
    fr1, relief=SUNKEN, bd=10,bg="lightblue")
doc.title("Дочернее окно")
doc.minsize(width=300, height=150)

comment = Label(doc, text="Тут можно что-нибудь написать",
                background="lightblue")
comment.grid(row=3,column=1)
tex = Text(
    doc,
    width=30, height=6,
    font="Arial 12",
    wrap=WORD
)
tex.grid(row=4, column=1, rowspan=2, columnspan=2)

c1 = IntVar()
ch1 = Checkbutton(doc, text="Сохранить вашу писанину?",
                  variable=c1, onvalue=1, offvalue=0, bg="lightblue")
ch1.grid(row=7, column=1)

def click_btn():
    doc.destroy()
    win2 = tk.Tk()
    win2.title("Дочернее окно №2")
    win2.geometry("300x300")

def calc_bmi():
    kg = int(weigh_tf.get())
    m = int(heig_tf.get()) / 100

    bmi = kg / (m * m)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        res = Label(result)
        res.grid(row=5, column=1)
        res.config(text=f'ИМТ = {bmi} Недостаточный вес')
    elif bmi > 18.5 and bmi < 24.9:
        res = Label(result)
        res.grid(row=5, column=1)
        res.config(text=f'ИМТ = {bmi} Нормальный вес')
    elif bmi > 24 and bmi < 29.9:
        res = Label(result)
        res.grid(row=5, column=1)
        res.config(text=f'ИМТ = {bmi} Избыточный вес')
    else:
        res = Label(result)
        res.grid(row=5, column=1)
        res.config(text=f'ИМТ = {bmi} Ожирение')

cal_btn = Button(
    fr1,
    text="Расчитать ИМТ",
    command=calc_bmi)
cal_btn.grid(row=5, column=2)

btn2 = Button(
    fr1, text="Пустое окно",
    command=click_btn
)
btn2.grid(row=6, column=2)

win.mainloop()