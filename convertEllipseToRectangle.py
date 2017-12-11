#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
import numpy as np
from math import *
import math
from PIL import Image

import cv2
import os

#Core codes come from https://github.com/ankanbansal/fddb-for-yolo/blob/master/convertEllipseToRect.py, 
#thank the author for his/her efforts.

def filterCoordinate(c,m):
    if c < 0:
    	return 0
    elif c > m:
    	return m
    else:
    	return c

def convertEllipseToRect(ellipseFilename, rectFilename):
    
    with open(ellipseFilename) as f:
            lines = [line.rstrip('\n') for line in f] #rstrip() 删除 string 字符串末尾的指定字符
    
    f = open(rectFilename,'wb')
    i = 0
    while i < len(lines):
        img_file = '/home/tianluchao/ProgramFiles/mtcnn/data/' + lines[i] + '.jpg'
        img = Image.open(img_file)
        img_cv=cv2.imread(img_file)
        w = img.size[0]
        h = img.size[1]
        num_faces = int(lines[i+1])
        for j in range(num_faces):
            ellipse = lines[i+2+j].split()[0:5]
            a = float(ellipse[0])
            b = float(ellipse[1])
            angle = float(ellipse[2])
            centre_x = float(ellipse[3])
            centre_y = float(ellipse[4])
            
            tan_t = -(b/a)*tan(angle)
            t = atan(tan_t)
            x1 = centre_x + (a*cos(t)*cos(angle) - b*sin(t)*sin(angle))
            x2 = centre_x + (a*cos(t+pi)*cos(angle) - b*sin(t+pi)*sin(angle))
            x_max = filterCoordinate(max(x1,x2),w)
            x_min = filterCoordinate(min(x1,x2),w)
            
            if tan(angle) != 0:
                tan_t = (b/a)*(1/tan(angle))
            else:
                tan_t = (b/a)*(1/(tan(angle)+0.0001))
            t = atan(tan_t)
            y1 = centre_y + (b*sin(t)*cos(angle) + a*cos(t)*sin(angle))
            y2 = centre_y + (b*sin(t+pi)*cos(angle) + a*cos(t+pi)*sin(angle))
            y_max = filterCoordinate(max(y1,y2),h)
            y_min = filterCoordinate(min(y1,y2),h)
        
            text = img_file + '\n' + str(x_min) + ' ' + str(y_min) + ' ' + str(abs(x_max-x_min)) + ' ' + str(abs(y_max-y_min)) + '\n'
            f.write(text)

            #another method to calculate the rectangle surrounding the ellipse
            # rectH = 2*a*(math.cos(math.radians(abs(angle))))
            # rectW = 2*b*(math.cos(math.radians(abs(angle))))

            # lx = int(max(0, centre_x - rectW/2))
            # ly = int(max(0, centre_y - rectH/2))
            # rx = int(min(w-1, centre_x + rectW/2))
            # ry = int(min(h-1, centre_y + rectH/2))

            # #show the converted bounding box on the image
            # cv2.rectangle(img_cv, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0,255,0), 5)
            # #cv2.rectangle(img_cv, (int(lx), int(ly)), (int(rx), int(ry)), (0,0,255), 3) #red
            # #cv2.ellipse(img_cv, (int(centre_x),int(centre_y)),(int(b),int(a)),int(angle),0,360,(0,0,255),-1) #show the ellipse
            # cv2.imshow('img', img_cv)
            # cv2.waitKey(1000)

        i = i + num_faces + 2

    f.close()

def main():

    for i in range(1,11):
        fileElliName="FDDB-fold-%02d-ellipseList.txt" %i
        fileRectName="FDDB-fold-%02d-rectList.txt" %i

        ellipseFilename = '/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/'+fileElliName
        rectFilename = '/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/'+fileRectName
        
        convertEllipseToRect(ellipseFilename, rectFilename)

if __name__=='__main__':
    main()
