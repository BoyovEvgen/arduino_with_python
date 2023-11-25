import time
import tkinter as tk
from tkinter import ttk
from ports import get_connected_ports
import serial_script
import firmata_script


class Gui:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Arduino Voltmetr')
        self.win.geometry("970x400")
        self.win.config(bg='#EBD4B5')

        tk.Button(self.win, text='Scan ports', command=self.reset).place(x=20, y=30)
        tk.Label(self.win, text="*Оновіть порти, якщо під'єднали Ардуіно після запуску програми.", font='Arial 10', bg='#EBD4B5') \
            .place(x=130, y=35)

        tk.Label(self.win, text="Виберіть порт для отримання данних: ", font='Arial 14', bg='#EBD4B5').place(x=20, y=80)
        self.check_port = ttk.Combobox(values=get_connected_ports())
        self.check_port.place(x=370, y=80)

        tk.Label(self.win, text="Виберіть як отримати данні: ", font='Arial 14', bg='#EBD4B5')\
            .place(x=20, y=130)
        self.check_script = ttk.Combobox(width=70,
                                         values=("1.Скріпт на ардуіно відправляє виміряну напругу в серіал.",
                                               "2.Працює скрипт на Пайтоні і спілкується з ардуіно через бібліотеку Firmata"))
        self.check_script.place(x=370, y=130)

        tk.Label(self.win, text="Виберіть NPLС: ", font='Arial 14', bg='#EBD4B5')\
            .place(x=20, y=180)
        self.nplc = []
        self.nplc.append(ttk.Combobox(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), width=5))
        self.nplc[0].place(x=370, y=180)
        self.nplc[0].set('0')
        self.nplc.append(ttk.Combobox(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), width=5))
        self.nplc[1].place(x=450, y=180)
        self.nplc[1].set('0')
        self.nplc.append(ttk.Combobox(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), width=5))
        self.nplc[2].place(x=530, y=180)
        self.nplc[2].set('0')
        tk.Label(self.win, text="*час вимірювання залежить від максимального значення.", font='Arial 10', bg='#EBD4B5') \
            .place(x=600, y=180)

        tk.Label(self.win, text="Результати вимірювання, V: ", font='Arial 14', bg='#EBD4B5')\
            .place(x=20, y=230)
        self.result = []
        self.result.append(tk.Label(self.win, font='Arial 12', width=5, bg='#FDF0D5'))
        self.result[0].place(x=370, y=230)
        self.result.append(tk.Label(self.win, font='Arial 12', width=5, bg='#FDF0D5'))
        self.result[1].place(x=450, y=230)
        self.result.append(tk.Label(self.win, font='Arial 12', width=5, bg='#FDF0D5'))
        self.result[2].place(x=530, y=230)

        tk.Button(self.win, text='GET VOLTAGE', command=self.callback).place(x=20, y=350)
        self.get_voltage = (serial_script.get_voltage, firmata_script.get_voltage)

    def callback(self):
        max_npls = max(int(item.get()) for item in self.nplc)
        port = self.check_port.get()
        script = self.check_script.get()[0]if self.check_script.get() else None
        if port != '' and script:
            measurements = self.get_voltage[int(script)-1](port, max_npls)
            self.set_results(measurements)
        return

    def set_results(self, measurements):
        for index in range(len(self.nplc)):
            nplc = int(self.nplc[index].get())
            if nplc > 0:
                sum_volt = sum(measurements[index] for index in range(nplc))
                result = round(sum_volt / nplc, 2)
                self.result[index].config(text=result)

    def reset(self):
        self.check_port = ttk.Combobox(values=get_connected_ports())
        self.check_port.place(x=370, y=80)

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    gui = Gui()
    gui.run()


