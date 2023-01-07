import tkinter as tk
# ボタンの文字を変更する関数
def call():
  btn.configure(text='変わります')
# 以下の二行でウィンドウの作成・サイズ設定
root = tk.Tk()
root.geometry('500x300')

# ラベルの作成
lbl = tk.Label(text='test')
btn = tk.Button(text='ボタンを押すと', command=call)

# ラベルの配置
lbl.pack()
btn.pack()

# 命令が動き始める
tk.mainloop()
