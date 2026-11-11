<<<<<<< HEAD
'''
We are going to ues a Python library like qrcode and convert url to qr
'''
import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
=======
'''
We are going to ues a Python library like qrcode and convert url to qr
'''
import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
img.save(filename)