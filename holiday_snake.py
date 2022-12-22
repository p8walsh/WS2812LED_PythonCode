import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

def snake(section_size, color_list):
    clength = len(color_list)
    for j in range(num_pixels):
        for k in range(len(color_list)):
            for i in range((k*int(num_pixels/clength)+j)%num_pixels, (k*int(num_pixels/clength)+section_size+j)%num_pixels):
                pixels[i] = color_list[k]
        pixels.show()
        time.sleep(0.001)

if __name__ == "__main__":
   
    section_size = int(num_pixels/10)
    color_list = [(255, 255, 255), (0, 255, 0), (255, 0, 0)]
    while True:
        snake(section_size, color_list)
    
        
