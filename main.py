from math import floor
from PIL import Image
from sys import argv

image = Image.open(argv[1]).rotate(90, Image.NEAREST, expand = 1).resize((17, 107))
pixels = list(image.getdata())

def find_k_value(pixels):
	k = 0

	for i, pixel in enumerate(pixels):
		if sum(pixel) / 3 <= 200:
			k += 2 ** i

	return k * 17

k = find_k_value(pixels)

def tuppers_formula(x, y):
	return 0.5 < floor((y // 17 // 2 ** (17 * floor(x) + floor(y) % 17)) % 2)

for y in range(k, k+17):
	for x in range(107, -1, -1):
		if tuppers_formula(x, y):
			print('██', end='')
		else:
			print('  ', end='')
	print('')

print(f'\n\nk-value: {k}')