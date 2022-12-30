import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

x = 0
while True: 
    for i in range(0, num_pixels-10, 10):
        for j in range(10):
            if ( i % 2 == x ):
                pixels[i+j] = (255, 205, 0)
            else:
                pixels[i+j] = (0, 0, 0)
    
    pixels.show()
    time.sleep(0.1)
    
    x = (x + 1) % 2
