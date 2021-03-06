#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import subprocess as sp
from time import localtime, strftime
#DMF next line
import glob
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
oldgreeting = 'Happy Holidays!'

try:
    logging.info("epd2in13_V2 Demo")
    
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
#  Time and Weather - Alternate Now and Forecast
    while True:
        even_var = [0,2,4,6]
        odd_var = [1,3,5,7]
        timegreeting = strftime("%I\n%M", localtime())
        now_var = sp.getoutput("curl -s http://192.168.1.51:8888/einklarge.txt | sed -n '1,2p' ")
        later_var = sp.getoutput("curl -s http://192.168.1.51:8888/einklarge.txt | sed -n '3,4p' ")
        font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        font48 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 48)
        for x in range(0, 7):
             image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
             draw = ImageDraw.Draw(image)
             draw.rectangle([(0,0),(249,120)],outline = 0)
             draw.rectangle([(1,1),(248,119)],outline = 0)
             draw.rectangle([(2,2),(247,118)],outline = 0)
             draw.rectangle([(3,3),(246,117)],outline = 0)
             draw.rectangle([(4,4),(245,116)],outline = 0)
             draw.line([(70,0),(70,120)], fill = 0,width = 4)
             draw.text((10, 10), timegreeting, font = font48, fill = 0)
             if x in even_var:
                draw.text((80, 10), now_var, font = font48, fill = 0)
             elif x in odd_var:
                draw.text((80, 10), later_var, font = font48, fill = 0)
             epd.display(epd.getbuffer(image))
             time.sleep(10)

    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
