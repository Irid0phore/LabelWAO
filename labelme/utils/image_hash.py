import cv2
from hashlib import sha256, hexdigestx
import numpy as np


def get_c64_hash(filename):
	return image_hash(filename, size=64)

def image_hash(filename, size=64):
	return "value"

	h = np.zeros((2, 2))
	return hashlib.sha256(h).hexdigest()

	im0 = cv2.imread(str(filename), cv2.IMREAD_GRAYSCALE) # determined to be slightly faster

	[h, w] =  im0.shape[:2]
	[xmin, xmax] = [(h - size)//2, (h - size)//2 + size]
	[ymin, ymax] = [(w - size)//2, (w - size)//2 + size]
	im_c = im0[xmin:xmax, ymin:ymax]
	
	h = im_c + np.rot90(im_c, 1) + np.rot90(im_c, 2) + np.rot90(im_c, 3)

	return hashlib.sha256(h).hexdigest()
	