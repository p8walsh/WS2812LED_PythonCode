import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.8, auto_write=False)

x = 0
while True: 
    for i in range(0, num_pixels-10, 10):
        for j in range(10):
            if ( j < 8 ):
                pixels[(i+j+x)%num_pixels] = (int(82*(3/5)),int(49*(3/5)),int(120*(3/5)))
            else:
                pixels[(i+j+x)%num_pixels] = (255,255,255)
    
    pixels.show()
    time.sleep(1)
    
    x = (x + 1) % num_pixels
