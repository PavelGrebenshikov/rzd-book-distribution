import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import json
import os
from functions import display_window, dev_window


window = tk.Tk()

# Установка размера окна приложения
ws = (window.winfo_screenwidth()/2) - (1200/2)
hs = (window.winfo_screenheight()/2) - (700/2)
window.geometry("1200x700")

# Название приложения
window.title("РЖД. Выдача и учет книг промеров.")

# Устанавливаем иконки приложения
window.iconbitmap("./icons/RZD.ico")

# Размер статический
window.resizable(0, 0)


# main block

# Фреймы
frame1 = tk.LabelFrame(width=1200, height=100, borderwidth=0, highlightthickness=0)
frame2 = tk.LabelFrame(width=1200, height=600, padx=10, pady=10, borderwidth=0, highlightthickness=0)
frame3 = tk.LabelFrame(frame2, width=250, height=600, padx=10, pady=10, borderwidth=0, highlightthickness=0)
frame4 = tk.LabelFrame(frame2, width=950, height=600, padx=10, pady=10, borderwidth=0, highlightthickness=0)
frame5 = tk.LabelFrame(frame4, width=950, height=20, padx=10, pady=10)
frame6 = tk.LabelFrame(frame4, width=950, height=600, padx=10, pady=10)

# Текстовые метки
LOGO_RZD = ImageTk.PhotoImage(Image.open("./icons/RZD.png"))
LABEL_LOGO = ttk.Label(frame1, image=LOGO_RZD)


LABEL_STYLE = ttk.Style()
LABEL_STYLE.configure("LABEL_TITLE_STYLE.TLabel", font="Arial 14", padding=10, width=120)
LABEL_TITLE = ttk.Label(frame1, text="Воронежская дистанция пути", style="LABEL_TITLE_STYLE.TLabel")
LABEL_TITLE.place(x=300, y=300)

LABEL_TITLE_ID = ttk.Label(frame5, text="ID", width=31)
LABEL_TITLE_BOOK = ttk.Label(frame5, text="Книга", width=31)
LABEL_TITLE_SECTIONS = ttk.Label(frame5, text="Линейный участок", width=31)
LABEL_TITLE_FULLNANME = ttk.Label(frame5, text="Кому выдан: ФИО", width=31)
LABEL_TITLE_DATE = ttk.Label(frame5, text="Дата выдачи", width=31)

# Отображение меток

LABEL_LOGO.grid(column=0, row=0, padx=10, pady=10)
LABEL_TITLE.grid(column=1, row=0, padx=0, pady=0)

LABEL_TITLE_ID.grid(column=0, row=0)
LABEL_TITLE_BOOK.grid(column=1, row=0)
LABEL_TITLE_SECTIONS.grid(column=2, row=0)
LABEL_TITLE_FULLNANME.grid(column=3, row=0)
LABEL_TITLE_DATE.grid(column=4, row=0)

# Функция удаления элемента из listbox
def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

# Отображение данных при запуске программы
if os.path.exists("./data/data.json"):
    with open("./data/data.json", "r+") as read_file:
        data = json.load(read_file)
    data_list = []
    for item_id in range(len(data)):
        data_string = f"{data[item_id]['id']}" + "                                             " + f"{data[item_id]['book']}" + "                                                 " + f"{data[item_id]['sections']}"  + "                  " + f"{data[item_id]['fullname']}"  + "       " +  f"{data[item_id]['date']}\n"
        data_list.append(data_string)

    languages_var = tk.StringVar(value=data_list[::-1])
    listbox = tk.Listbox(frame6, listvariable=languages_var, width=95, height=30, font="Arial 12")
    listbox.pack(side="left", fill="both", expand=1)
            
    scrollbar = ttk.Scrollbar(frame6, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y", padx=10, pady=10)
            
    listbox["yscrollcommand"]=scrollbar.set

# Обновление окна
def update_window():
    if os.path.exists("./data/data.json"):

        with open("./data/data.json", "r+") as read_file:
            data = json.load(read_file)

        # Удаление из listbox всех элементов
        listbox.delete(0, listbox.size())

        for item_id in range(len(data)):
            data_string = f"{data[item_id]['id']}" + "                                             " + f"{data[item_id]['book']}" + "                                                 " + f"{data[item_id]['sections']}"  + "                  " + f"{data[item_id]['fullname']}"  + "       " +  f"{data[item_id]['date']}"
            listbox.insert(0, data_string)

# Кнопки

BUTTON_ADD = tk.Button(frame3, width=13, height=1, font="Arial 12", text="Добавить", command=display_window, cursor="hand2")
BUTTON_EDIT = tk.Button(frame3, width=13, height=1, font="Arial 12", text="Изменить", cursor="hand2")
BUTTON_DELETED = tk.Button(frame3, width=13, height=1, font="Arial 12", text="Удалить", cursor="hand2", command=delete)
BUTTON_UPDATE = tk.Button(frame3, width=13, height=1, font="Arial 12", text="Обновить", cursor="hand2", command=update_window)
BUTTON_DEV = tk.Button(frame3,  width=13, height=1, font="Arial 12", text="Разработчик", cursor="hand2", command=dev_window)

# Отображение кнопок
BUTTON_ADD.grid(column=0, row=0, padx=10, pady=10)
BUTTON_EDIT.grid(column=0, row=1, padx=10, pady=10)
BUTTON_DELETED.grid(column=0, row=2, padx=10, pady=10)
BUTTON_UPDATE.grid(column=0, row=3, padx=10, pady=10)
BUTTON_DEV.grid(column=0, row=4, padx=10, pady=10)

# Отображение
frame1.pack()
frame2.pack(anchor='w', padx=10)
frame3.pack(side="left", padx=10, pady=10, anchor='n')
frame4.pack(side="left", padx=10, pady=10)
frame5.pack(padx=10, pady=10)
frame6.pack(padx=10, pady=10)

window.mainloop()