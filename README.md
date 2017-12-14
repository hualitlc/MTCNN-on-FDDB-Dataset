# MTCNN-on-FDDB-Dataset
Using Caffe and python to reproduce the results of MTCNN on FDDB dataset.



### References
0. The implementation of [MTCNN](https://github.com/kpzhang93/MTCNN_face_detection_alignment) using python & caffe, thank the author [DuinoDu/mtcnn](https://github.com/DuinoDu/mtcnn).
1. (alternatively) We can convert the ellipse annotations into the rectangle annotations for better visualization. Thank the author [ankanbansal/fddb-for-yolo](https://github.com/ankanbansal/fddb-for-yolo/blob/master/convertEllipseToRect.py).



### Better visualization
We can use the **convertEllipseToRectangle.py** to convert the FDDB-folds/FDDB-fold-01-ellipseList.txt into FDDB-folds/FDDB-fold-01-rectList.txt and show the converted bounding boxes on the images.



### Run MTCNN on general image
We can use the **demo.py** to run mtcnn framwork on general images. This file comes from [DuinoDu/mtcnn/demo.py](https://github.com/DuinoDu/mtcnn/blob/master/demo.py).



### Run MTCNN on FDDB dataset
We can use the **runFDDB.py** to run mtcnn framwork on [FDDB dataset](http://vis-www.cs.umass.edu/fddb/). Core codes come from [DuinoDu/mtcnn/demo.py](https://github.com/DuinoDu/mtcnn/blob/master/demo.py).



### The official evaluation of your results
Download the official [evaluation code](http://vis-www.cs.umass.edu/fddb/results.html#eval) and use the commond 'make' in the evaluation folder.
To evaluate the results/preditions of your framework, just use the following codes.
```
./evaluate -a ../data/FDDB-folds/ellipseList.txt -d ../data/FDDB-folds/predict.txt -l ../data/FDDB-folds/foldList.txt -f 0
```
Then tempContROC.txt and tempDiscROC.txt will be generated in the /data/FDDB-folds/.



### Draw the ROC curves
0. Install the toolbox [Gnuplot](http://www.gnuplot.info/).
1. Using the following commond.
```
gnuplot contROC.p 
gnuplot discROC.p
```
We will get the tempContROC-MTCNN.png(tempDiscROC-MTCNN.png) and the ROC curves like this:
![image](https://github.com/hualitlc/MTCNN-on-FDDB-Dataset/blob/master/FDDB-folds/tempContROC-MTCNN.png)
![image](https://github.com/hualitlc/MTCNN-on-FDDB-Dataset/blob/master/FDDB-folds/tempDiscROC-MTCNN.png)



### Citation
    @article{7553523,
        author={K. Zhang and Z. Zhang and Z. Li and Y. Qiao}, 
        journal={IEEE Signal Processing Letters}, 
        title={Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks}, 
        year={2016}, 
        volume={23}, 
        number={10}, 
        pages={1499-1503}, 
        keywords={Benchmark testing;Computer architecture;Convolution;Detectors;Face;Face detection;Training;Cascaded convolutional neural network (CNN);face alignment;face detection}, 
        doi={10.1109/LSP.2016.2603342}, 
        ISSN={1070-9908}, 
        month={Oct}
    }
