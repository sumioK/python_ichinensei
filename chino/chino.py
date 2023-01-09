import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

import sklearn.datasets
import sklearn.svm
import numpy

def imageToData(filename):
  grayImage = PIL.Image.open(filename).cover('L')
  grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
  