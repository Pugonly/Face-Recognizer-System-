# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:56:16 2018

@author: stonesword
"""

from PIL import Image
import os

#path = r"./Face Database"
path = r"./testData"

for filename in os.listdir(path):
    if(filename[0] == 's'):
        test = Image.open(path+'\\'+filename)
        test = test.resize((180,240),Image.BILINEAR)
        test.save(path+'\\'+filename)