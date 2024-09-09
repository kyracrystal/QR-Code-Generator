import qrcode
from pathlib import Path

website_link = input('Enter the website link for QR Code: ')

qr = qrcode.QRCode(version = int(input('Enter the version of the QR Code // controls size of QR Code [1-40 def: 1]: ')), box_size = int(input('Enter the box-size of the QR Code // controls pixel size of boxes in QR Code [def: 5]: ')), border = int(input('Enter the border parameters of the QR Code // controls how many boxes thick the border of the QR Code is [def: 5]: ')))
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('rename-me-qr.png')
Path("rename-me-qr.png").rename("generated-codes/rename-me-qr.png")
print('QR Code generated successfully :3')
print('Remember to rename the QR Code in the /generated-codes/ folder') 