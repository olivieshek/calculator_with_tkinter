import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):

    def calculate_currency(self, var):
        try:
            int(self.money.get())
        except ValueError:
            self.money.delete(0, "end")
            messagebox.showwarning(
                'Некоректная сумма!',
                'Введите целое число или десятичную дробЬ!'
            )
        else:
            user_money = int(self.money.get())
            rate = self.var.get()
            result = round(user_money / rate, 2)
            self.result_label.config(text=result)

        
    def __init__(self):
        super().__init__()
        # параметры окна
        self.geometry('400x500')  # размер окна;
        self.title('Мой Калькулятор Валют')  # заголовок окна;

        # текст пользователю
        self.text0 = tk.Label(
            self,
            text='Введите сумму в [RUB] российских рублях:'
        )
        self.text0.pack()
        
        # поле ввода суммы
        self.money = tk.Entry(
            self,
            width=20,
            font='Arial 14',
            bd=3
        )
        self.money.pack()
        # валюты
        self.var = tk.DoubleVar()
        self.var.set(75.74)
        # доллар
        self.usd = tk.Radiobutton(
            self,
            text='[USD] Доллар США',
            variable=self.var,
            value=75.74
        )
        self.usd.pack()
        # евро
        self.eur = tk.Radiobutton(
            self,
            text='[EUR] Евро',
            variable=self.var,
            value=86.72
        )
        self.eur.pack()
        # гривна
        self.uah = tk.Radiobutton(
            self,
            text='[UAH] Украинская гривна',
            variable=self.var,
            value=2.69
        )
        self.uah.pack()

        # кнопка
        self.button0 = tk.Button(
            self, text='Конвертировать',
            width=20, height=2,
            fg=''
        )
        self.button0['command'] = lambda: self.calculate_currency(self.var)
        self.button0.pack()

        # выведение результата
        self.text1 = tk.Label(self, text='Результат ниже:', font='Arial 14')
        self.text1.pack()
        # итоговый вывод
        self.result_label = tk.Label(
            self, 
            text='', 
            font='Arial 14',
            fg='green'
        )
        self.result_label.pack()


if __name__ == '__main__':
    window = Calculator()
    window.mainloop()