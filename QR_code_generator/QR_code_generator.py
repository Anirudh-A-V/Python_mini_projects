import pyqrcode 
from pyqrcode import QRCode
import png
  
# String which represent the QR code 
s = input("Enter the url : ").strip()
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png("Web_design.png", scale = 8) 