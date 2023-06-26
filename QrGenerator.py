import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_H,
               box_size=10, border=4)

user = input("Enter your Link: ")
color = "black"
bgColor = "white"
color = input("Enter your qr color: ")
bgColor = input("Enter your Baclkground color: ")


qr.add_data(user)
qr.make(fit=True)
img = qr.make_image(fill_color=color, back_color=bgColor)
img.save("Qrcode.png")