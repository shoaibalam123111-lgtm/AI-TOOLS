import qrcode

qr = qrcode.make("https://chatgpt.com/c/69e9be16-ec34-83e8-a7ac-0b3bdf88347e")
qr.save("my_qr.png")

print("QR Code generated successfully!")