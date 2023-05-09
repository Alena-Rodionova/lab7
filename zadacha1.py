import PIL
from PIL import Image

filename = "gumons2.png"
with Image.open(filename) as img:
    img.load()

img.show()
width, height = img.size

format = img.format

mode = img.mode

print("Размеры: ", width,"*", height)
print("Формат: ", format)
print("Цветовая модель:", mode)