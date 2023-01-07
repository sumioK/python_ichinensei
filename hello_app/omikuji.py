import random
import tkinter as tk
kuji = ['大吉', '吉', '小吉', '凶']

root = tk.Tk()
root.geometry('400x400')

def choose():
  lbl.configure(text=random.choice(kuji))

def reset():
  lbl.configure(text='くじを引く')

lbl = tk.Label(text='結果は...')
btn = tk.Button(text='くじを引く', command=choose)
rebtn = tk.Button(text='reset', command=reset)

lbl.pack()
btn.pack()
rebtn.pack()
tk.mainloop()