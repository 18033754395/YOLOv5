import os
import random


trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = 'G:/yolov5-master/xml_txt/Annotations'
txtsavepath = 'G:/yolov5-master/xml_txt/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('G:/yolov5-master/xml_txt/ImageSets/trainval.txt', 'w')
ftest = open('G:/yolov5-master/xml_txt/ImageSets/test.txt', 'w')
ftrain = open('G:/yolov5-master/xml_txt/ImageSets/train.txt', 'w')
fval = open('G:/yolov5-master/xml_txt/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
