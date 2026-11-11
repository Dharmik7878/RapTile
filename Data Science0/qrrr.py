<<<<<<< HEAD
import qrcode

url = input("Enter the URL: ")
filename = input("Enter the filename: ")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
=======
import qrcode

url = input("Enter the URL: ")
filename = input("Enter the filename: ")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
img.save(filename)