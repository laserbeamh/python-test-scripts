#!/usr/bin/env python3
import tkinter as tk

x = 0

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there["text"] = "Click me"
    self.hi_there.pack(side="top")
    self.hi_there["command"] = self.counter

    self.quit = tk.Button(self, text="Close", fg="red", command=self.master.destroy)
    self.quit.pack(side="bottom")

  def counter(self):
    global x
    x += 1
    print(x)

root = tk.Tk()
root.title("Button")

label = tk.Label(root, text = "Hello World!").pack()
app = Application(master=root)
app.mainloop()


score = 0
