import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x500')  # размер окна;
        self.title('Мой Калькулятор Валют')  # заголовок окна;

        self.text0 = tk.Label(self,
                            text='Введите сумму в [RUB] российских рублях:')
        self.textbox0 = tk.Entry(self,
                                width=20,
                                font='Arial 14',
                                bd=3)
        var = tk.IntVar()
        var.set(0)   
        self.usd = tk.Radiobutton(self, text='[USD] Доллар США', variable=var, value=0)
        self.eur = tk.Radiobutton(self, text='[EUR] Евро', variable=var, value=1)
        self.uah = tk.Radiobutton(self, text='[UAH] Украинская гривна', variable=var, value=2)
        self.button0 = tk.Button(self, text='Конвертировать',
                                width=20, height=2,
                                bg='grey', fg='black')
        self.text1 = tk.Label(self, text='Результат ниже:', font='Arial 14')
        # self.result = tk.Label(self, text='', font='Arial 14')  # FIXME: пихать сюда результат

        self.text0.pack()
        self.textbox0.pack()
        self.usd.pack()
        self.eur.pack()
        self.uah.pack()
        self.button0.pack()
        self.text1.pack()
        # self.result.pack() # TODO: сначала на 24 строке


if __name__ == '__main__':
    window = Calculator()
    window.mainloop()