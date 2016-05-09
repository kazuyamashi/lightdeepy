#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import sys
import os.path
import os

def detect(filename, cascade_file = "cascade/lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    i = 0
    dir = filename.split(".")
    dir2 = dir[len(dir)-2].translate(None,".").split("/")
    path = dir2[len(dir2)-1]
    os.makedirs(path)
    for (x, y, w, h) in faces:
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print "%s %s %s %s"%(x, y, w, h)
        dst = image[y:y+h, x:x+w]
        cv2.imwrite("%s/%s.png"%(path,i), dst)
        i = i + 1

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)

detect(sys.argv[1])
