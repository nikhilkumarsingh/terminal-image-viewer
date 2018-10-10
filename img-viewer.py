import sys
import numpy as np
from PIL import Image


def get_ansi_color_code(r, g, b):
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))


def show_image(img_path):
	try:
		img = Image.open(img_path)
	except FileNotFoundError:
		exit('Image not found.')

	h = 100
	w = int((img.width / img.height) * h)

	img = img.resize((w,h), Image.ANTIALIAS)
	img_arr = np.asarray(img)
	h,w,c = img_arr.shape

	for x in range(h):
	    for y in range(w):
	        pix = img_arr[x][y]
	        print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
	    print()


if __name__ == '__main__':
	if len(sys.argv) > 1:
		img_path = sys.argv[1]
		show_image(img_path)