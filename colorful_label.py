from PIL import Image
from imutils import paths 
import random

image_path = sorted(list(paths.list_images("label")))       

cnt=0

print("[INFO] Start processing image...")
for image_path in image_path:
	cnt += 1
 
	# random color component
	a = random.randint(0, 255)
	b = random.randint(0, 255)
	c = random.randint(0, 255)

	img = Image.open(image_path)
	img = img.convert("RGBA")     
	pixdata = img.load()
	for y in range(img.size[1]):
    		for x in range(img.size[0]):
        		if pixdata[x, y] == (0, 0, 0, 255):
            			pixdata[x, y] = (a, b, c, 255)    	
	img.save("colorful_label/" + str(cnt) + '.png', format = 'png')
print("[INFO] Finish processing...")
