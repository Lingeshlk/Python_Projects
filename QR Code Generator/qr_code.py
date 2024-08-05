import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

qr.add_data("https://teamwebq-6ab4596fb749.herokuapp.com/")
qr.make(fit=True)
img=qr.make_image(fill_colar='black',back_color='white')

img.save('webpage.png')
