import board
import neopixel
import time
import random

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.8, auto_write=False)

def slow_change(indices, cur_color, new_color):
	# Slowly fade to black
	for i in range(255):
		for index in indices:
			pixels[index] = (255 - i)*(cur_color) / 255
		pixels.show()
	
	# Slowly fade in new color
	for i in range(255):
		for index in indices:
			pixels[index] = (i)*(new_color) / 255
		pixels.show()

while True:
	# Start with all green
	for i in range(num_pixels):
		pixels[i] = (0, 255, 0)
	# Get 20% random pixels
	pixel_list = []
	for i in range(num_pixels):
		pixel_list.append(i)
	indices = []
	for j in range(1, 6):
		for i in range(j*int(num_pixels)/5):
			choice = random.choice(pixel_list)
			pixel_list.remove(choice)
			indices.append(choice)
		slow_change(indices, (0, 255, 0), (255, 0, 0))
		time.sleep(2)
		
		