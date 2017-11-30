#coding=utf-8
from PIL import Image, ImageDraw, ImageFont

sourceFileName = "source.jpg"

avatar         = Image.open(sourceFileName)
drawAvatar     = ImageDraw.Draw(avatar)

xSize, ySize = avatar.size
fontSize     = min(xSize, ySize) // 11

font_path = 'C:\\WINDOWS\\Fonts\\simsunb.ttf'

myFont       = ImageFont.truetype(font_path,int(fontSize*1.5))

drawAvatar.text([0.85 * xSize - fontSize, 0.15 * ySize - fontSize],"99+", fill = (255, 0, 0), font = myFont)
del drawAvatar

save_path = ''

avatar.save(save_path)