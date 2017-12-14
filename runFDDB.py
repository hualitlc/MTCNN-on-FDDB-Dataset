#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
import numpy as np
from math import *
import math
#from PIL import Image

import cv2
import os
import demo

#import _init_paths
import caffe


def main():

    minsize = 20
    
    caffe_model_path = "/home/tianluchao/ProgramFiles/mtcnn/model"
    threshold = [0.6, 0.7, 0.7]
    factor = 0.709

    caffe.set_mode_gpu()
    PNet = caffe.Net(caffe_model_path+"/det1.prototxt", caffe_model_path+"/det1.caffemodel", caffe.TEST)
    RNet = caffe.Net(caffe_model_path+"/det2.prototxt", caffe_model_path+"/det2.caffemodel", caffe.TEST)
    ONet = caffe.Net(caffe_model_path+"/det3.prototxt", caffe_model_path+"/det3.caffemodel", caffe.TEST)
    
    for i in range(1,11):

        '''
        faceListInt.txt: the difference is foutOnce.write(imgpath+'\n'), pointer---foutOnce
        foldList.txt: the difference is foutFold.write(imgpath+'\r'), we adopt this file as the final file list input, pointer---foutFold
        FDDB-fold-01.txt-FDDB-fold-10.txt: input the file list, pointer---f
        FDDB-fold-01-out.txt-FDDB-fold-10-out.txt: detection result, and we copy the 10 FDDB-fold-%02d-out.txt into "predict.txt", pointer---fout
        '''

        #fileElliName="FDDB-fold-%02d-ellipseList.txt" %i
        fileOutName="FDDB-fold-%02d-out.txt" %i
        fileFoldName="FDDB-fold-%02d.txt" %i

        #ellipseFilename = '/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/'+fileElliName
        outFilename = '/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/' + 'predict.txt'#fileOutName
        foldFilename = '/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/' + fileFoldName

        fileOutNameOnce="/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/faceListInt.txt"
        fileOutFileList="/home/tianluchao/ProgramFiles/mtcnn/data/FDDB-folds/foldList.txt"
      
        prefixFilename = '/home/tianluchao/ProgramFiles/mtcnn/data/'

        fout = open(outFilename,'a+')
        #foutOnce = open(fileOutNameOnce, "a+") #faceListInt.txt, the difference is foutOnce.write(imgpath+'\n')
        #foutFold = open(fileOutFileList, "a+") #foldList.txt, the difference is foutFold.write(imgpath+'\r'), we adopt this file as the final file list input

        #error = []
        f = open(foldFilename, 'r') #FDDB-fold-00.txt, read
        for imgpath in f.readlines():
            
            imgpath = imgpath.split('\n')[0]
            #foutOnce.write(imgpath+'\n')
            #foutFold.write(imgpath+'\r')
            img = cv2.imread(prefixFilename+imgpath+'.jpg')
            if img is None:
                continue
            img_matlab = img.copy()
            tmp = img_matlab[:,:,2].copy()
            img_matlab[:,:,2] = img_matlab[:,:,0]
            img_matlab[:,:,0] = tmp

            # check rgb position
            #tic()
            boundingboxes, points = demo.detect_face(img_matlab, minsize, PNet, RNet, ONet, threshold, False, factor)
            #print "the score is: %s" %points
            #toc()

            # # copy img to positive folder
            # if boundingboxes.shape[0] > 0 :
            #    import shutil
            #    shutil.copy(imgpath, '/home/duino/Videos/3/disdata/positive/'+os.path.split(imgpath)[1] )
            # else:
            #    import shutil
            #    shutil.copy(imgpath, '/home/duino/Videos/3/disdata/negetive/'+os.path.split(imgpath)[1] )

            # useless org source use wrong values from boundingboxes,case uselsee rect is drawed 
            #    for i in range(len(boundingboxes)):
            #        cv2.rectangle(img, (int(boundingboxes[i][0]), int(boundingboxes[i][1])), (int(boundingboxes[i][2]), int(boundingboxes[i][3])), (0,255,0), 1)    

            # img = demo.drawBoxes(img, boundingboxes)
            # cv2.imshow('img', img)
            # #ch = cv2.waitKey(0) & 0xFF
            # #if ch == 27:
            # #    break
            # cv2.waitKey(1000)

            '''
            To be recognized by the evaluation code, the detection
            output is expected in the following format:
            <image name i>
            <number of faces in this image =im>
            <face i1>
            <face i2>
            ...
            <face im>
            ...

            where the representation of a face depends on the specifics
            of the shape of the hypothesized image region. The evaluation
            code supports the following shapes:
  
            4 a. Rectangular regions
                Each face region is represented as:
                <left_x top_y width height detection_score> 
            4 b. Elliptical regions
                Each face region is represented as:
                <major_axis_radius minor_axis_radius angle center_x center_y detection_score>.
            '''

            text1 = str(imgpath)+'\n'+str(len(boundingboxes))+'\n'
            fout.write(text1) #FDDB-fold-%02d-out.txt or predict.txt

            for coordinate in range(len(boundingboxes)):               
                text2 = str(int(boundingboxes[coordinate][0])) + ' ' + str(int(boundingboxes[coordinate][1])) + ' ' \
                + str(abs(int(boundingboxes[coordinate][2]-boundingboxes[coordinate][0]))) + ' ' \
                + str(abs(int(boundingboxes[coordinate][3]-boundingboxes[coordinate][1]))) + ' ' \
                + str(boundingboxes[coordinate][4]) + '\n'
                
                fout.write(text2) #FDDB-fold-%02d-out.txt or predict.txt


            #if boundingboxes.shape[0] > 0:
            #    error.append[imgpath]
        #print error
        f.close() #input the fold list, FDDB-fold-00.txt
        fout.close() #output the result, predict.txt
        #foutOnce.close() #faceListInt.txt, the difference is foutOnce.write(imgpath+'\n')
        #foutFold.close() #foldList.txt, the difference is foutFold.write(imgpath+'\r'), we adopt this file as the final file list input
        
    #runFDDB(ellipseFilename, rectFilename)

if __name__=='__main__':
    main()
