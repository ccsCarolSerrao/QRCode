
import pyqrcode

qr = pyqrcode.create("https://github.com/ccsCarolSerrao/QRCode")
print(qr.text())
print(qr.terminal(module_color='red', background='yellow'))
print(qr.terminal(module_color=5, background=123, quiet_zone=1))


qr.png("site.png", scale=10)

