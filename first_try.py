import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r-g-b back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.01)
'''i = 0
while True:
    index = i % 150
    if i > 150:
        i = 0
    for j in range(0,142,8):
        for k in range(j, j+4):
            pixels[k] = (255, 255, 255)
        for k in range(j+4, j+8):
            pixels[k] = (0, 0, 0)

    for j in range(0,142,8):
        for k in range(j, j+4):
            pixels[k] = (255, 0, 0)
        for k in range(j+4, j+8):
            pixels[k] = (0, 0, 255)

    #time.sleep(2)

    i = i + 10
'''
