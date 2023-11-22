from PIL import Image#处理图像

#打开图片
img = Image.open("image.jpg")
#值越大，颜色越浅，越白 > 字符越疏散 > 越趋于右边
#值越小，颜色越深，越黑 > 字符越密集 > 越趋于左边
out = img.convert("L")        #将图片转化为灰度图L
# out.show()

#L = R * 299/1000 + G * 587/1000 + B * 114/1000
# 拿像素点的颜色值： px
# px = om.getpixel((0,0))         #拿到(0.0)位置的颜色
#拿到所有像素点的位置的颜色值 > 转化为字符
width,height = out.size          #获得图片的大小

out = out.resize((int(width ),int(height )))

width,height = out.size
ascii = '@%#*+=-. '
texts = ""
print(width)
print(height)
print(out.size)
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        texts += ascii[int(gray / 255 * 8)]
    texts += "\n"
with open("C:/Users/lxy/Desktop/Huskie.txt","w") as file :
    file.write(texts)


