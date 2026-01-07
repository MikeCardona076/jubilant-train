import qrcode


mitexto = input("Ingrese el texto o enlace para el código QR: ")
img = qrcode.make(mitexto)
miimagen = input("Ingrese el nombre del archivo para guardar el código QR: ")
img.save(miimagen + ".png")