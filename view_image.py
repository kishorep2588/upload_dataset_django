import json
import requests
from PIL import Image
from io import BytesIO

json_file_name = 'electronics_product.json'

with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)

size = (450, 300)

def make_square(im, min_size=300, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    #size = min(min_size, x, y)
    size = min_size
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int(abs(size - x) / 2), int(abs(size - y) / 2)))
    return new_im

count = 0
for item in data:
    if count == 16:
        break
    count += 1
    image_data = item['image']
    content = requests.get(image_data)
    image = Image.open(BytesIO(content.content))
    new_image = image.resize(size)
    #new_image = make_square(image)
    #new_image.save(f'/uploads/products/{str(count)}.jpg')
    #image.save(f'/uploads/products/{str(count)}.jpg')
    #image.show()
    new_image.save(f'images/{str(count)}.png')