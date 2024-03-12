import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import json
import os

def get_date():
    date_now = datetime.datetime.now()
    return f"{date_now.year}-{date_now.month}-{date_now.day}"

def display_window():

    # Переменная содержащая названия выдаваемых книг 
    BOOKS = ["ПУ-28", "ПУ-29", "ПУ-30"]
    LINEAR_SECTIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    FRAME_SIZE_WIDTH = 700
    FRAME_SIZE_HEIGHT = 100
    second_window = tk.Toplevel()
    
    # Функция для закрытия окна
    def closed_window():
        if messagebox.askokcancel("Закрытие окна", "Хотите закрыть данное окно?"):
            second_window.destroy()

    # Установка размера окна приложения
    second_window.geometry("700x140")

    # Название приложения
    second_window.title("РЖД. Выдача и учет книг промеров. Добавление записи.")

    # Закрытие окна
    second_window.protocol("WM_DELETE_WINDOW", closed_window)
    # Устанавливаем иконки приложения
    second_window.iconbitmap("./icons/RZD.ico")

    # Фиксированое окно
    second_window.resizable(0, 0)

    # Фреймы
    frame1 = tk.LabelFrame(second_window, width=FRAME_SIZE_WIDTH, height=FRAME_SIZE_HEIGHT, borderwidth=0, highlightthickness=0)
    frame2 = tk.LabelFrame(frame1, width=FRAME_SIZE_WIDTH, height=FRAME_SIZE_HEIGHT, borderwidth=0, highlightthickness=0)
    frame3 = tk.LabelFrame(frame1, width=FRAME_SIZE_WIDTH, height=FRAME_SIZE_HEIGHT, borderwidth=0, highlightthickness=0)
    frame4 = tk.LabelFrame(frame1, width=FRAME_SIZE_WIDTH, height=FRAME_SIZE_HEIGHT, borderwidth=0, highlightthickness=0)

    # Метки

    label = tk.Label(frame2, text="Книга", width=30)
    label_1 = tk.Label(frame2, text="Линейный участок", width=30)
    label_2 = tk.Label(frame2, text="Кому выдано: ФИО", width=30)

    # Сombobox

    combobox = ttk.Combobox(frame3, values=BOOKS, width=31)
    combobox.current(0)
    combobox.grid(column=0, row=0, padx=15, pady=10)

    combobox_1 = ttk.Combobox(frame3, values=LINEAR_SECTIONS, width=31)
    combobox_1.current(0)
    combobox_1.grid(column=1, row=0, padx=15, pady=10)

    # Поле для ввода данных

    input_user = tk.Entry(frame3, width=31)
    input_user.grid(column=2, row=0, padx=15, pady=10)

    # Отображение меток
    label.grid(column=0, row=0, padx=10, pady=10)
    label_1.grid(column=1, row=0, padx=10, pady=10)
    label_2.grid(column=2, row=0, padx=10, pady=10)

    # Кнопка сохранения
    button = tk.Button(frame4, text="Сохранить", command=lambda: save_data(0, book=combobox.get(),
                        sections=combobox_1.get(), fullname=input_user.get(), date=get_date()))
    button.pack(side="right")


    # Отображение фрейма
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack(anchor="e", padx=15, pady=15)


def save_data(id, book, sections, fullname, date):

    if os.path.exists("./data/data.json"):
          with open("./data/data.json", "r+") as read_file:
            data = json.load(read_file)
            data.append({"id": id, "book": book, "sections": sections, "fullname": fullname, "date": date})

          with open("./data/data.json", "w+") as write_file:
            json.dump(data, write_file, indent=4)

    else:
        data = {"id": id, "book": book, "sections": sections, "fullname": fullname, "date": date}
        with open("./data/data.json", "w+") as file:
            json.dump([data], file, indent=4)


# окно разработчика
def dev_window():
    dev_window = tk.Toplevel()

    # Установка размера окна приложения
    dev_window.geometry("700x140")

    # Название приложения
    dev_window.title("Разработчик приложения.")

    # Устанавливаем иконки приложения
    dev_window.iconbitmap("./icons/RZD.ico")

    # Фиксированое окно
    dev_window.resizable(0, 0)

    LABEL_ABOUT_DEV = tk.Label(dev_window, text="Разработчик: Гребенщиков Павел Сергеевич", font="Arial 14", justify="center", height=10)
    LABEL_ABOUT_DEV.pack()