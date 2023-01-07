import board
import neopixel
import time

num_pixels = 150
pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False)

#We're going to make a Betel inspired script <3

#Betel Colors: "black", white, pink
black_pixels = (0, 0, 0)
white_pixels = (255,255,255) 
pink_pixels = (255, 16, 240)

#set the pixels ...
for i in range(150):
  if(i%4 == 0):
    pixels[i] = black_pixels
  elif(i%4 == 1):
    pixels[i] = white_pixels
  elif(i%4 == 2):
    pixels[i] = black_pixels
  elif(i%4 == 3):
    pixels[i] = pink_pixels
    
#light it up!
pixels.show()
