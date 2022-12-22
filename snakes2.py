import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)
        
rainbow = [(255,0,0),(255,40,0),(40,255,0),(0,255,0),(0,255,40),(0,40,255),(0,0,255)]

while True:
    section_size = int(num_pixels/len(rainbow))
    
    for j in range(num_pixels):
        for color in range(len(rainbow)):
            for k in range((0+(color*section_size)+j)%num_pixels,(section_size+(color*section_size)+j)%num_pixels):
                pixels[k] = rainbow[color]


        pixels.show()
        time.sleep(0.0001)
