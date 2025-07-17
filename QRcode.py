#Generate a QR code using Python


import qrcode


data = "https://www.instagram.com/devv_016?igsh=c3p1YWx5OTBrbnJx"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR code Generated Successfully!")