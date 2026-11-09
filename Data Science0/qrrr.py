import qrcode

url = input("Enter the URL: ")
filename = input("Enter the filename: ")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)