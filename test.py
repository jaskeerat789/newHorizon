from luma.core.interface.serial import i2c,spi
from luma.core.render import canvas
from luma.oled.device import ssd1331
import os
from PIL import Image
import time 
serial=spi(device=0,port=0)
device=ssd1331(serial)
def ABC(i):
	img=Image.open(os.getcwd()+'/ALPHABETS/'+i+'.png').convert("RGBA")
	fff=Image.new(img.mode,img.size,(255,)*4)
	background=Image.new("RGBA",device.size,"white")
	posn=((device.width-img.width)//2,0)
	background.paste(img,posn)
	device.display(background.convert(device.mode))
	time.sleep(5)
	device.clear()
def text():
	with canvas(device) as draw:
		draw.rectangle(device.bounding_box,outline="white",fill="black")
		draw.text((30,40),"A",fill="white")

#print(dir(device))

