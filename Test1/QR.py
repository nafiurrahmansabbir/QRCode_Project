import qrcode as qr

print("****** QR-Code Generator Program *****")
data=input("Enter Your Link: ")
num=input("Save As: ")

img=qr.make(data)
img.save(f"{num} CreatQR.png")
