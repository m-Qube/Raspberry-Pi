from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True
blue = (0, 0, 255)

def b():
  B = blue
  logo = [
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B, 
  ]
  return logo

images = [b]
count = 0

while True:
  s.set_pixels(images[count % len(images)]())
  time.sleep(.75)
  count += 1
