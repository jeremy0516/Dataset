from PIL import Image
from imutils import paths
import random

image_Path = sorted(list(paths.list_images("colorful_label")))

cnt = 0

for image_path in image_Path:
	cnt += 1
	degree = random.randint(0, 360)
	img = Image.open(image_path)
	img = img.rotate(degree, Image.BILINEAR)
	img.save("rotated_label/" + str(cnt) + '.png', format = 'png')

