
from PIL import Image
from imutils import paths
import pickle
import random
random.seed(42)
import cv2
import os
import numpy as np

# load the path of label & background
lab_image_Path = sorted(list(paths.list_images("rotated_label")))
random.shuffle(lab_image_Path)
bac_image_Path = sorted(list(paths.list_images("background")))
random.shuffle(bac_image_Path)

# create a list of size/location/letter
labels = []
data = []
letter_list = []
labels_letter = []

cnt = 0

# processing
print("[INFO] Start processing image...")
for bac_image_path in bac_image_Path:
	bac = Image.open(bac_image_path)
	w_bac, h_bac = bac.size

	lab_image_path = random.choice(lab_image_Path)
	label = Image.open(lab_image_path)
	w_lab, h_lab = label.size	

	# randomly change the color of letter
		
			
	# randomly resize the letter
	w_re = random.randint(40, 160)
	h_re = random.randint(30, 120)
	label = label.resize((w_re, h_re))
	w_re, h_re = label.size

	# paste the letter on background in random location
	x = random.randint(0, w_bac-w_re)
	y = random.randint(0, h_bac-h_re)
	label.thumbnail((w_re, h_re))
	bac.paste(label,(x, y), label)		
	
	# save image
	cnt += 1
	bac.save("dataset/" + str(cnt) + ".png", format = "png")		

	# record the letters' size & their origin coordinate
	let = [w_re/256, h_re/256, x/256, y/256]
	labels.append(let)

	# record the image size
	ima = cv2.imread("dataset/{}.png".format(cnt))
	data.append(ima)
	
	# record which letter it is
	index = ord(os.path.split(lab_image_path)[-2][-1]) - ord('Z')
	for i in range(25):
		letter_list.append(0)
	if index != 0:
		letter_list.insert(index,1)
	else:
		letter_list.append(1)
	labels_letter.append(letter_list[-26:])	

# print(labels)
# data = np.array(data)
# print(data.shape)
# print(labels_letter[0])
# print(labels_letter[1])
# print(labels_letter[2])
# print(labels_letter[3])

print("[INFO] Finish processing...")

# save the label list
print("[INFO] Save labels...")
with open("labels.pickle","wb") as file:
	pickle.dump(labels,file)
with open("dataset.pickle","wb") as file:
	pickle.dump(data,file)
with open("letter.pickle","wb") as file:
	pickle.dump(labels_letter,file)

