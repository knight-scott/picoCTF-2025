import stepic
from PIL import Image

img = Image.open('upz.png')
data = stepic.decode(img)
print(data)