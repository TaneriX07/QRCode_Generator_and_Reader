import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import tkinter.filedialog

def generate_qrcode():
    text = input("Enter a text to be converted: ")
    name = input("What do you want to name the file? ")

    # Create QR Code
    qr = pyqrcode.create(text)
    qr.png(f"{name}.png", scale=8)

    print("QR Code created successfully!")

def read_qrcode():
    file = tkinter.filedialog.askopenfilename(title="Select Image", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg")))
    d = decode(Image.open(file))
    print(d[0].data.decode())

mode = input("1.Generate QRCode\n2.Read QRCode\nPlease enter 1 or 2: ")
if mode == "1":
    generate_qrcode()
elif mode == "2":
    read_qrcode()
else:
    print("Please enter either 1 or 2")
