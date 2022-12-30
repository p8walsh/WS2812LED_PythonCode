import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.8, auto_write=False)

x = 0
while True: 
    for i in range(0, num_pixels-10, 10):
        for j in range(10):
            if ( j < 5 ):
                pixels[(i+j+x)%num_pixels] = (255,205,0)
            else:
                pixels[(i+j+x)%num_pixels] = (40,40,40)
    
    pixels.show()
    time.sleep(1)
    
    x = (x + 1) % num_pixels
