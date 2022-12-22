import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r-g-b back to r.
    if pos < 0:
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
    elif pos < 255:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    else:
        return wheel(pos - 255)
    return (r, g, b)

j = 0
while True:
    if j > 255:
        j = 0
            
    for i in range(num_pixels):
        pixels[i] = wheel(i+j) 
    pixels.show()
    time.sleep(0.001)
    j = j + 1
