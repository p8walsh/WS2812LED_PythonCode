import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

j = 0
x = 0
y = x + 1
while True: 
    for i in range(0, num_pixels-10, 10):
        for j in range(10):
            if ( i % 3 == x ):
                pixels[i+j] = (0, 255, 0)
            elif ( i % 3 == y ):
                pixels[i+j] = (255, 0, 0)
            else:
                pixels[i+j] = (255, 255, 255)
    
    pixels.show()
    time.sleep(0.1)
    
    x = (x + 1) % 3
    y = (y + 1) % 3
