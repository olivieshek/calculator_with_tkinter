import tkinter as tk

class Calculator(tk.Tk):
    def calculate_currency(var
    ):
        user_money = int(money.get())
        rate = var.get()
        result = round(user_money / rate, 2)
        result_label.config(text=result)

    def __init__(self):
        super().__init__()
        # параметры окна
        self.geometry('400x500')  # размер окна;
        self.title('Мой Калькулятор Валют')  # заголовок окна;
        # текст пользователю
        self.text0 = tk.Label(self,
                            text='Введите сумму в [RUB] российских рублях:')
        # поле ввода суммы
        self.money = tk.Entry(self,
                            width=20,
                            font='Arial 14',
                            bd=3)
        var = tk.DoubleVar()
        var.set(75.74)
        self.usd = tk.Radiobutton(self, text='[USD] Доллар США', variable=var, value=75.74)
        self.eur = tk.Radiobutton(self, text='[EUR] Евро', variable=var, value=86.72)
        self.uah = tk.Radiobutton(self, text='[UAH] Украинская гривна', variable=var, value=2.69)
        self.button0 = tk.Button(self, text='Конвертировать',
                                width=20, height=2,
                                bg='grey', fg='black')
        self.button0['command'] = Calculator.calculate_currency(var)
        self.text1 = tk.Label(self, text='Результат ниже:', font='Arial 14')
        self.result_label = tk.Label(self, text='', font='Arial 14')

        self.text0.pack()
        self.money.pack()
        self.usd.pack()
        self.eur.pack()
        self.uah.pack()
        self.button0.pack()
        self.text1.pack()
        self.result_label.pack()


if __name__ == '__main__':
    window = Calculator()
    window.mainloop()