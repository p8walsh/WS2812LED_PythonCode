import board
import neopixel
import time
import sys
import signal

def end(pixels):
    pixels.fill((0, 0, 0))
    pixels.show()
    sys.exit(0)

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

christmas_colors = [(0, 255, 0), (255, 0, 0), (255, 255, 255)]
hanukkah_colors = [(0, 0, 255), (255, 255, 255), (0, 0, 255)]
kwanzaa_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 0)]

color_list = []
color_list.append(christmas_colors)
color_list.append(hanukkah_colors)
color_list.append(kwanzaa_colors)

signal.signal(signal.SIGKILL, end(pixels))
signal.signal(signal.SIGINT, end(pixels))

j = 0
k = 0
x = 0
y = x + 1
z = 0
while True: 
    for i in range(0, num_pixels-10, 10):
        for j in range(10):
            if ( i % 3 == x ):
                pixels[i+j] = color_list[z][0]
            elif ( i % 3 == y ):
                pixels[i+j] = color_list[z][1]
            else:
                pixels[i+j] = color_list[z][2]
    
    pixels.show()
    time.sleep(0.5)
    
    x = (x + 1) % 3
    y = (y + 1) % 3
    k = k + 1
    if (k % 150) == 0:
        z = (z + 1) % 3
