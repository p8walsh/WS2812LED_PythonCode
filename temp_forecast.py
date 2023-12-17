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

currentTime = time.localtime()

def end(signum, frame):
#    pixels.fill((0, 0, 0))
#    pixels.show()
    sys.exit(0)

signal.signal(signal.SIGTERM, end)
signal.signal(signal.SIGINT, end)

  
if __name__ == '__main__':
    colors = []  
    # Get the colors corresponding to the temperature graph for the current hour 
    with open(sys.path[0] + "\\" + time.strftime("TemperatureColorsDenver_%Y_%m_%d_%H.txt",currentTime), 'r') as f:
        for line in f:
            splitline = line.split(',')
            colors.append(splitline)

    # Colors example after previous and before subsequent: ['0.07273877292852624', ' 0.9901960784313726', ' 0.8950031625553447', ' 1.0', ' \n']
    # Need only first 3 numbers, which should be multiplied by 255 and rounded
    for i in range(len(colors)):
        colors[i].pop()
        colors[i].pop()
        for j in range(len(colors[i])):
            colors[i][j] = round(float(colors[i][j]) * 255)
    
    # Now colors is a 2-d array of the correct colors: [35, 255, 212]
    for i in range(len(pixels)):
        pixels[i] = colors[i]