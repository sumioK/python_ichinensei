import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

import sklearn.datasets
import sklearn.svm
import numpy

def imageToData(filename):
  # 画像を８ｘ８のグレースケールに変換
  grayImage = PIL.Image.open(filename).convert('L')
  grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
  # 画像をイメージラベルに表示する
  dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300), resample=0))
  imageLabel.configure(image = dispImage)
  imageLabel.image = dispImage
  # 画像を数値リストに変換する
  numImage = numpy.asarray(grayImage, dtype = float)
  numImage = 16 - numpy.floor(17 * numImage / 256)
  numImage = numImage.flatten()
  return numImage

def predictDigits(data):
  digits = sklearn.datasets.load_digits()

  clf = sklearn.svm.SVC(gamma = 0.001)
  clf.fit(digits.data, digits.target)

  n = clf.predict([data])
  textLabel.configure(text = 'この画像は' + str(n) + 'です')

def openFile():
  fpath = fd.askopenfilename()
  if fpath:
    data = imageToData(fpath)
    predictDigits(data)

root = tk.Tk()
root.geometry('400x400')

btn = tk.Button(root, text='Open File', command = openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

textLabel = tk.Label(text='手書きの数字を認識します！')
textLabel.pack()

tk.mainloop()
