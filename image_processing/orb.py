#!/usr/bin/python
# -*- coding: utf-8 -*-
# orb.py
# described by Kazushi Yamashina

import cv2
import sys


if __name__ == '__main__':

	argvs = sys.argv
	argc = len(argvs)
	if argc	!= 2:
		print "Usage: ./orb.py input_file"
		quit()
	input_file = argvs[1]

	img = cv2.imread(input_file)
	# アルゴリズム名を引数で渡す
	detector = cv2.FeatureDetector_create('ORB')
	keypoints = detector.detect(img)
	print len(keypoints)
	# fo = open("result.txt",'w')
	# for i in xrange(0,len(keypoints)):
	# 	str = "%s"%keypoints[i]
	# 	fo.write(str.translate(None,"<KeyPoint>"))
	# 画像への特徴点の書き込み
	# out = cv2.drawKeypoints(img, keypoints, None)
	# 表示
	# cv2.imshow('name', out)
	# cv2.waitKey(0)