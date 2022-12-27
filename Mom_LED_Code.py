import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

for x in range (0, num_pixels-8, 8):
	pixels[x]=(255,255,255)
	pixels[x+1]=(255,0,0)
	pixels[x+2]=(255,0,0)
	pixels[x+3]=(0,255,0)
	pixels[x+4]=(255,255,0)
	pixels[x+5]=(255,255,255)
	pixels[x+6]=(255,0,255)
	pixels[x+7]=(0,255,255)
pixels.show()