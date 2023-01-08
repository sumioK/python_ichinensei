import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

# 画像ファイルを数値リストに変換
def imageToData(filename):
  # 画像を8*8のグレースケールに変換
  grayImage = PIL.Image.open(filename).convert('L')
  grayImage = grayImage.resize((8, 8),PIL.Image.Resampling.LANCZOS)

  # 画像を8*8のリストに変換
  numImage = numpy.asarray(grayImage, dtype = float)
  # asarrayは0-255の数値に変換するため、0-16に変換する
  numImage = 16 - numpy.floor(17 * numImage /256)
  numImage = numImage.flatten()

  return numImage

# 数値を予測する関数
def predicDigits(data):
  # 学習データを読み込む
  digits = sklearn.datasets.load_digits()
  # データを使って学習する
  clf = sklearn.svm.SVC(gamma=0.001)
  clf.fit(digits.data, digits.target)
  # 予測結果を表示する
  n = clf.predict([data])
  print("予測＝", n)

data = imageToData("image.png")

predicDigits(data)
