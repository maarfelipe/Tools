from tkinter import *
import pyautogui
import time

class Clicker:
    def __init__(self, root):
        self.root = root
        root.geometry('250x260')
        root.title('Clicker da Bubs')

        self.running = False
        self.counting = False
        self.last_click = 0
        self.remaining = 60
        self.clicks = 0
        self.last_update = time.time()
        self.start_time = time.time()

        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

        self.inner_frame = Frame(self.frame)
        self.inner_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.click_button = Button(self.inner_frame, text='CLICAR', command=self.start, width=8)
        self.click_button.config(font=('Arial', 22, 'bold'))

        self.stop_button = Button(self.inner_frame, text='STOP', command=self.stop, width=8)
        self.stop_button.config(font=('Arial', 18))

        self.clicks_label = Label(self.inner_frame, text='Clicks: 0')
        self.clicks_label.config(font=('Arial', 14))

        self.label = Label(self.inner_frame, text=f'Next click: {int(self.remaining)}s')
        self.label.config(font=('Arial', 14))

        self.time_label = Label(self.inner_frame, text='Time: 00m:00s')
        self.time_label.config(font=('Arial', 14))

        self.click_button.pack(side=TOP, pady=8)
        self.stop_button.pack(side=TOP, pady=8)
        self.clicks_label.pack(side=TOP, pady=8)
        self.label.pack(side=TOP, pady=8)
        self.time_label.pack(side=TOP, pady=8)


    def start(self):
        if self.running:
            return
        self.running = True
        self.counting = True
        self.last_click = time.time()
        self.update_label()
        self.click()

    def stop(self):
        if not self.running:
            return
        self.running = False
        self.counting = False
        self.last_click = 0
        self.clicks = 0
        self.remaining = 60
        self.label.config(text=f'Next click: {int(self.remaining)}s')
        self.clicks_label.config(text='Clicks: 0')
        self.start_time = time.time()

    def update_label(self):
        if not self.counting:
            return
        now = time.time()
        time_since_last_update = now - self.last_update
        self.last_update = now
        self.remaining -= time_since_last_update
        if self.remaining <= 0:
            self.remaining = 60
        self.label.config(text=f'Next click: {int(self.remaining)}s')
        self.clicks_label.config(text=f'Clicks: {self.clicks}')

        elapsed_time = int(now - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        time_str = f'{minutes:02d}m:{seconds:02d}s'
        self.time_label.config(text=f'Time: {time_str}')

        self.label.after(1000, self.update_label)

    def click(self):
        if not self.running:
            return
        if time.time() - self.last_click >= 60:
            pyautogui.click()
            self.last_click = time.time()
            self.clicks += 1
        self.root.after(60000, self.click)


root = Tk()
clicker = Clicker(root)

root.mainloop()