
from PIL import Image
from imutils import paths 

image_path = sorted(list(paths.list_images("letters")))       

cnt=0

print("[INFO] Start processing image...")
for image_path in image_path:
	cnt += 1
	img = Image.open(image_path)
	img = img.convert("RGBA")     
	pixdata = img.load()
	for y in range(img.size[1]):         
		for x in range(img.size[0]):             
			if pixdata[x,y][0]>220 and pixdata[x,y][1]>220 and pixdata[x,y][2]>220 and pixdata[x,y][3]>220:                 
				pixdata[x, y] = (255, 255, 255, 0)     
				img.save("label/" + str(cnt) + '.png', format = 'png')
print("[INFO] Finish processing...")
