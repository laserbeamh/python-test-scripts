#!/usr/bin/env python3
import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.hi_there = tk.Button(self)

    self.quit = tk.Button(self, text="Close", fg="red", command=self.master.destroy)
    self.quit.pack(side="bottom")

root = tk.Tk()
root.title("Puppies!")

label = tk.Label(root, text = "Puppies Galore!").pack()
app = Application(master=root)
app.mainloop()
