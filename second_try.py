import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

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

while True:
    section_size = int(num_pixels/10)
    
    for j in range(num_pixels):
        for i in range(num_pixels):
            pixels[i] = (255, 255, 255)
        for i in range(0+j, (section_size+j)%num_pixels):
            pixels[i] = (255, 0, 0) 
        for i in range((int(num_pixels/3)+j)%num_pixels, (int(num_pixels/3)+section_size+j)%num_pixels):
            pixels[i] = (0, 0, 255)
        for i in range((2*int(num_pixels/3)+j)%num_pixels, (2*int(num_pixels/3)+section_size+j)%num_pixels):
            pixels[i] = (255, 0, 0)
        
        pixels.show()
        time.sleep(0.0001)
