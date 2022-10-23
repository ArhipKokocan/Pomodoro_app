import tkinter as tk
from tkinter import ttk, PhotoImage
import time
import threading


class PomodoroApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title('PomodoroTimer')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="png_files/but-one-thing-all-tomatoes-have-in-common-tomato-115636129320xdejuvxub.png"))

        self.s = ttk.Style()

        self.s.configure("TNotebook.Tab", font=('Mythias', 14))
        self.s.configure('TButton', font=('Mythias', 14))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', pady=10, padx=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='Long Break')
        self.tabs.add(self.tab3, text='Short Break')


        self.root.mainloop()


    def start_timer_threat(self):
        pass

    def start_timer(self):
        pass

    def reset_timer(self):
        pass


    def skip_timer(self):
        pass



PomodoroApp()
