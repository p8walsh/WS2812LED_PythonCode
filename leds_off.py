import neopixel
import board
import time

numLEDS = 300
pixels = neopixel.NeoPixel(board.D18, numLEDS)

pixels.fill((0, 0, 0))
