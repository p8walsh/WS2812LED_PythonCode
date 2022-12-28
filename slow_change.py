import board
import neopixel
import time
import random
import copy
import signal
import sys

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels,
                           brightness=0.8, auto_write=False)

colors =[(255, 0, 0),
         (3, 240, 252),
         (0, 0, 255),
         (0, 255, 0),
         (117, 2, 106),
         (0, 0, 255)
        ]

def end(signum, frame):
    pixels.fill((0, 0, 0))
    pixels.show()
    sys.exit(0)

signal.signal(signal.SIGTERM, end)
signal.signal(signal.SIGINT, end)
    
def slow_change(indices, cur_color, new_color):
    r, g, b = cur_color
    # Slowly fade to black
    for i in range(255):
        for index in indices:
            pixels[index] = (int(((255 - i) * r) / 255),
                             int(((255 - i) * g) / 255), int(((255 - i) * b) / 255))
        pixels.show()
        #time.sleep(0.0001)

    r, g, b = new_color
    # Slowly fade in new color
    for i in range(255):
        for index in indices:
            pixels[index] = (int(((i) * r) / 255),
                             int(((i) * g) / 255), int(((i) * b) / 255))
        pixels.show()
        #time.sleep(0.0001)

def loop_slow_change(cur_color, new_color):
    pixel_list = []
    for i in range(num_pixels):
        pixel_list.append(i)
    for j in range(1, 6):
        indices = []
        for i in range(int(num_pixels/5)):
            choice = random.choice(pixel_list)
            pixel_list.remove(choice)
            indices.append(choice)
        slow_change(indices, cur_color, new_color)
        
if __name__ == '__main__':
    mutable_colors = []
    cur_color = colors[0]
    while True:
        if len(mutable_colors) == 0:
            mutable_colors = copy.deepcopy(colors)
        new_color = random.choice(mutable_colors)
        mutable_colors.remove(new_color)
        loop_slow_change(cur_color, new_color)
        cur_color = new_color
