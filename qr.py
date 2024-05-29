# making a qr code
# scan this to get restaurant menu
import qrcode

qrcode_image = qrcode.make("https://127.0.0.1:8000")
qrcode_image.save("QR_code.png")