from tkinter import *
from PIL import ImageTk, Image
import pyqrcode
from pyqrcode import QRCode
import cairosvg
import time
import os

CUR_DIR = os.getcwd()

def CreateImg():
    # String which represent the QR code
    s = textentry.get()

    # Generate QR code
    url = pyqrcode.create(s)

    # Create and save the png file naming "myqr.png"
    url.svg("myqr.svg", scale=8)
    time.sleep(1)
    cairosvg.svg2png(url='myqr.svg', write_to='image.png')
    time.sleep(1)
    im = Image.open(CUR_DIR+"/image.png")
    im.show()


window = Tk()

window.title("My QR GENERATOR")
window.configure(background="black")


# Label 2
Label(window, text="Enter the link you want for the QR Code", bg="black",
      fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

# Create Text Entry Box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# Submit
Button(window, text="SUBMIT", width=6, command=CreateImg).grid(
    row=3, column=0, sticky=W)


window.mainloop()
