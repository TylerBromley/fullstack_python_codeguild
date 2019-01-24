# lab16-image-manipulation_v3.py

from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

circle_x = width/2
circle_y = height/6
circle_radius = 50
line_width = 20
x0 = 250
y0 = 100
x1 = 250
y1 = 330

draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='blue')
draw.line((x0, y0, x1, y1), fill='blue', width=line_width)
draw.line((x0+5, y0+50, x1-150, y1-120), fill='blue', width=line_width)
draw.line((x0+5, y0+50, x1+150, y1-120), fill='blue', width=line_width)
draw.line((x0, y0+210, x1-190, y1+130), fill='blue', width=line_width)
draw.line((x0, y0+210, x1+190, y1+130), fill='blue', width=line_width)


img.show()