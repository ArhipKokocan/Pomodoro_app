import tkinter as tk
from tkinter import ttk, PhotoImage
import time
import threading


class PomodoroApp:

    def __init__(self):
        self.root = tk.Tk()

        self.width = 600
        self.height = 300

        self.root.geometry(f"{self.width}x{self.height}+{450}+{250}")
        self.root.title('PomodoroTimer')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="png_files/but-one-thing-all-tomatoes-have-in-common-tomato-115636129320xdejuvxub.png"))

        self.s = ttk.Style()

        self.s.configure("TNotebook.Tab", font=('Mythias', 14))
        self.s.configure('TButton', font=('Mythias', 14))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomodoro_timer_lable = ttk.Label(self.tab1, text='25:00', font=('Mythias', 30))
        self.short_break_timer_lable = ttk.Label(self.tab2, text='05:00', font=('Mythias', 30))
        self.long_break_timer_lable = ttk.Label(self.tab3, text='15:00', font=('Mythias', 30))

        self.pomodoro_timer_lable.pack(pady=40)
        self.long_break_timer_lable.pack(pady=40)
        self.short_break_timer_lable.pack(pady=40)

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='Short Break')
        self.tabs.add(self.tab3, text='Long Break')

        self.grid = ttk.Frame(self.root)
        self.grid.pack(pady=20)

        self.start_button = ttk.Button(self.grid, text='Start', command=self.start_timer_threat)
        self.start_button.grid(row=0, column=0)


        self.skip_button = ttk.Button(self.grid, text='Skip', command=self.skip_timer)
        self.skip_button.grid(row=0, column=1)


        self.reset_button = ttk.Button(self.grid, text='Reset', command=self.reset_timer)
        self.reset_button.grid(row=0, column=2)

        self.stop_button = ttk.Button(self.grid, text='Stop', command=self.stop_timer)
        self.stop_button.grid(row=0, column=3)

        self.pomodoro_counter_lable = ttk.Label(self.grid, text='Pomodoros: 0', font=('Mythias', 14))
        self.pomodoro_counter_lable.grid(row=1, column=0, columnspan=4, pady=20)

        self.pomodoros = 0
        self.stop = False
        self.skip = False
        self.running = False


        self.root.mainloop()


    def start_timer_threat(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        if self.stop is True:
            self.stop = False
        self.skip = False
        self.stop = False
        timer = self.tabs.index(self.tabs.select()) + 1

        if timer == 1:
            all_seconds = 60 * 25

            while all_seconds > 0 and not self.stop:
                minutes, seconds = divmod(all_seconds, 60)
                self.pomodoro_timer_lable.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                all_seconds -= 1

            if not self.stop or self.skip:
                self.pomodoros += 1
                self.pomodoro_counter_lable.config(text=f"Pomodoro: {self.pomodoros}")

                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                    self.start_timer()
                else:
                    self.tabs.select(1)
                self.start_timer()

        elif timer == 2:
            all_seconds = 60 * 5

            while all_seconds > 0 and not self.stop:
                minutes, seconds = divmod(all_seconds, 60)
                self.short_break_timer_lable.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                all_seconds -= 1

            if not self.stop or self.skip:
                self.tabs.select(0)
                self.start_timer()

        elif timer == 3:
            all_seconds = 60 * 15

            while all_seconds > 0 and not self.stop:
                minutes, seconds = divmod(all_seconds, 60)
                self.long_break_timer_lable.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                all_seconds -= 1

            if not self.stop or self.skip:
                self.tabs.select(0)
                self.start_timer()
        else:
            print('Something went wrong')

    def reset_timer(self):
        self.stop = True
        self.skip = False
        self.pomodoros = 0
        self.pomodoro_timer_lable.config(text="25:00")
        self.short_break_timer_lable.config(text="05:00")
        self.long_break_timer_lable.config(text='15:00')
        self.pomodoro_counter_lable.config(text="Pomodoros: 0")
        self.running = False


    def skip_timer(self):
        current_tab = self.tabs.index(self.tabs.select())

        if current_tab == 0:
            self.pomodoro_timer_lable.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_lable.config(text='05:00')
        elif current_tab == 2:
            self.long_break_timer_lable.config(text='15:00')

        self.stop = True
        self.skip = True

    def stop_timer(self):
        self.stop = True
        self.running = False


if __name__ == '__main__':
    PomodoroApp()
