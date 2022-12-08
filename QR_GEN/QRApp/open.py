import cairosvg
from PIL import Image
cairosvg.svg2png(url='myqr.svg',write_to='image.png')

im = Image.open(r"/home/ved/Desktop/QR_GEN/QRApp/image.png")
im.show()
# A test file to check whether the CairoSVG works properly. 
# Test report is positive and can be used to convert SVG to PNG easily in a matter of 2 seconds!
