from PIL import Image
from main import *

qr1 = qr.QRCode(version = 1,
                error_correction = qr.constants.ERROR_CORRECT_H,
                box_size = 10, border= 4,)
qr1.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr1.make(fit=True)
img = qr1.make_image(fill_cocor = "red", back_color = "blue")
img.save("Youtube")