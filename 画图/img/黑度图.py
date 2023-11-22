from PIL import Image
img = Image.open("th.jpg")
out = img.convert("L")
out.show()