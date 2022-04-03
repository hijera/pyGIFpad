# -*- coding: cp1251 -*-
import random as r
import pygame as pg
import pygame.midi
import numpy as np
from PIL import Image
import launchpad_py as lppy
import re, sys, os
import time
import configparser


lib_launchpad_type = {
    1: lppy.Launchpad(),
    2: lppy.LaunchpadMk2(),
    3: lppy.LaunchpadMiniMk3(),
    4: lppy.LaunchpadLPX(),
    5: lppy.LaunchpadPro(),
    6: lppy.LaunchpadProMk3(),
    7: lppy.LaunchControl(),
    8: lppy.LaunchControlXL(),
    9: lppy.LaunchKeyMini(),
    10: lppy.Dicer()
}
max_w=12
max_h=12
lib_button_action= [[0 for x in range(max_w)] for y in range(max_h)] 
lib_button_decode= [[0 for x in range(max_w)] for y in range(max_h)]
config = configparser.ConfigParser()
config.read('config.ini')
print(config['DEFAULT']['defaultgif'])
lp_type=int(config['DEFAULT']['launchpad_type'])
sections=config.sections()

def drawimg(lp,img):

    x=1
    y=0
    for row in img:
        y=0
        for j in row:

            if lp_type==1:
                newj=j/64;
                lp.LedCtrlXY(y,x,int(newj[0]),int(newj[1]));
            else:
                newj=j/2;
                lp.LedCtrlXY(y,x,int(newj[0]),int(newj[1]),int(newj[2]))
            y+=1
        x+=1
    return

def decode_gif_file(filename):
    img = Image.open(filename)
    rgbimg=img
    iarr= []
    try:
        while True:
           iarr.append(np.array(rgbimg.resize((8,8), Image.ANTIALIAS).convert('RGB').copy()))
           img.seek(rgbimg.tell()+1)
    except EOFError:
        pass # end of sequence
    return iarr
#if len(sys.argv)<2 or not sys.argv[1]:
#    print('No filename specified. Pass it as parameter')
#    sys.exit()



for sect in sections:
    print(sect)
    result=re.match(r'CONFIG_BUTTON_([0-9])_([0-9])',sect)
    lib_button_action[int(result[1])][int(result[2])]=config[sect]['gif']
    lib_button_decode[int(result[1])][int(result[2])]=decode_gif_file(config['DEFAULT']['gif_folder']+'/'+config[sect]['gif']);

gdata=decode_gif_file(config['DEFAULT']['gif_folder']+'/'+config['DEFAULT']['defaultgif'])

gif=gdata


lp = lib_launchpad_type[lp_type]
lp.Open()

lp.Reset()
frame=0


spd=0.1
if config['DEFAULT']['frame_time']:
    spd=float(config['DEFAULT']['frame_time'])

while 1:
    gif=gdata
    for i in gif:
        drawimg(lp,i)
        frame+=1

        state_button=lp.ButtonStateXY()
        if state_button:
            print(state_button)
            item=lib_button_action[int(state_button[0])+1][int(state_button[1])]
            if item:
                frame=0

                target_name='CONFIG_BUTTON_'+str(state_button[0])+'_'+str(state_button[1])
                if config.has_section(target_name) and config[target_name]['frame_time']:
                    spd=float(config[target_name]['frame_time'])
                gdata=lib_button_decode[int(state_button[0])+1][int(state_button[1])]
                break
        time.sleep(spd)
#                gif=gdata
#                drawimg(lp,i)
#        inport=mido.open_input()
#        for msg in inport:
#            print(msg)
#        print(i)
#        time.sleep(1)
