from PIL import Image

#img = Image.open("./Medienarchiv_2.jpg")
#grayscaleimg = Image.new("L", img.size)
#grayscaleimg.paste(img)
#rgbimage = Image.new("RGB", img.size)
#rgbimage.paste(grayscaleimg)
#rgbimage.save('foo.jpg')

img = Image.open("./Medienarchiv_1.jpg")
rgbimg = Image.new("RGB", img.size)
rgbimg.paste(img)
rgbimg.save('Medienarchiv_2.jpg')
