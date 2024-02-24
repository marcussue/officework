import tkinter as tk
from tkinter import messagebox
import time

class FocusTimer:
    def __init__(self, master, focus_minutes):
        self.master = master
        self.focus_minutes = focus_minutes
        self.seconds_left = focus_minutes * 60

        self.label = tk.Label(master, text="")
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="开始专注", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="停止专注", command=self.stop_timer)
        self.stop_button.pack(pady=10)
        self.stop_button["state"] = "disabled"

    def start_timer(self):
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.countdown()

    def stop_timer(self):
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.master.after_cancel(self.timer_id)
        self.label.config(text="")
        self.seconds_left = self.focus_minutes * 60

    def countdown(self):
        if self.seconds_left > 0:
            minutes, seconds = divmod(self.seconds_left, 60)
            self.label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.seconds_left -= 1
            self.timer_id = self.master.after(1000, self.countdown)
        else:
            messagebox.showinfo("专注结束", "专注时间结束")
            self.stop_timer()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("专注时钟")
    
    focus_timer = FocusTimer(root, focus_minutes=25)
    
    root.mainloop()
