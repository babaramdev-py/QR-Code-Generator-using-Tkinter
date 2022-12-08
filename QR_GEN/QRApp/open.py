import cairosvg
from PIL import Image
cairosvg.svg2png(url='myqr.svg',write_to='image.png')

im = Image.open(r"/home/ved/Desktop/QR_GEN/QRApp/image.png")
im.show()
