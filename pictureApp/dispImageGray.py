import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def disPhoto(path):
  newImage = PIL.Image.open(path).convert("L").resize((300,300))

  imageData = PIL.ImageTk.PhotoImage(newImage)
  imageLabel.configure(image = imageData)
  imageLabel.image = imageData

def openFile():
  fpath = fd.askopenfilename()
  if fpath:
    disPhoto(fpath)


# 以下は画面の作成
root = tk.Tk()
root.geometry('400x350')

btn = tk.Button(text='ファイルを開く', command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()