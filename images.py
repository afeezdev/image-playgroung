from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", 'png')
filtered_img = img.convert('L')

crooked = filtered_img.rotate(90)
resize = filtered_img.resize((300,300))

filtered_img.save("grey.png", 'png')
crooked.save("crooked.png", "png")
resize.save('resize.png','png')
resize.show()


