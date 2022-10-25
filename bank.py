from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesnocancel
from tkinter.ttk import Checkbutton

def click():
    result =  askyesnocancel(title="Подтвержение операции", message="Подтвердить операцию?")
    if result==None: showinfo("Результат", "Операция приостановлена")
    elif result: showinfo("Результат", "Перевод выполнен / чек: 5748573409")
    else : showinfo("Результат", "Операция отменена")

window = Tk()
window.title("Банк Останься без штанов")
window.geometry('600x500')
lbl = Label(window, text="введите суму денег котроую хоитие перевести")
lbl.grid(column=0, row=5)
txt = Entry(window, width=15)
txt.grid(column=1, row=5)
lbl = Label(window, text="введите счет на котрый хотите первести денги")
lbl.grid(column=0, row=10)
txt = Entry(window, width=15)
txt.grid(column=1, row=10)
btn = Button(window, text='Перевести', command=click)
btn.grid(column=0, row=20)
lbl = Label(window, text="приложение сделано в развлекательных целях", font=("Arial Bold", 6))
lbl.grid(column=0, row=30)
window.mainloop()