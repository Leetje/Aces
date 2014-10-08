__author__ = 'leethomas'


from PIL import Image


im = Image.open("/Users/leethomas/PycharmProjects/Aces/Images/silhouette front.jpg")
#pix = im.load()
#im.rotate(45).show
#print(pix[1,1])
print(im.getcolors())

