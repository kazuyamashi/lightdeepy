#!/usr/bin/python
# -*- coding: utf-8 -*-
# learning_fisher.py
# described by Kazushi Yamashina
import sys
sys.path.append("../lib/")
import dnn
import math

if __name__ == '__main__':
	argvs = sys.argv
	argc = len(argvs)
	if argc	!= 3:
		print "Usage: ./learning_fisher.py input_file cycle_time"
		quit()

	dataFile = argvs[1]
	cycle_time = int(argvs[2])

	dnn = dnn.DNN({'numOfUnits':[4, 4, 4, 3]})

	dnn.setLearningCoefficient(0.001)

	input_file = open(dataFile, 'r')
	lines = []
	for str in input_file:
		line = str.split("\r\n")
		lines.append(line[0])

	size = int(math.floor(len(lines) / 10))

	allDataSets = []
	i = 0

	accuracySum = 0

	while True:
		dataSets = []

		for j in xrange(0, size):
			if i > (len(lines)-1):
				break
			ary = lines[i].split("\t")
			dataSets.append(ary)
			i = i + 1

		allDataSets.append(dataSets)

		if len(allDataSets) == 10:
			break
	for i in xrange(0, len(allDataSets)):

		trainData = []
		testData = []

		for j in xrange(0, len(allDataSets)):
			for k in xrange(0, len(allDataSets[j])):
				if i == j:
					testData.append(allDataSets[j][k])
				else:
					trainData.append(allDataSets[j][k])

		for l in xrange(0, cycle_time):

			inputData = []

			for m in xrange(0, len(trainData)):
				dataPart = []

				for n in xrange(1, len(trainData[m])):
					dataPart.append(float(trainData[m][n]))

				inputData.append({'expected': float(trainData[m][0]), 'data': dataPart})
			# print inputData
			dnn.train(inputData)

			result = dnn.test(inputData)

			if result < 0.01:
				break

		corrects = 0

		for o in xrange(0, len(testData)):
			dataPart = []
			for p in xrange(1, len(testData[o])):
				dataPart.append(float(testData[o][p]))
			result = dnn.predict(dataPart)
			# print result
			# print testData[o][0]
			if result['best'] == int(testData[o][0]):
				corrects = corrects + 1

		accuracySum += 100 * corrects / len(testData)

	print "accuracy: %s%%"%(accuracySum / len(allDataSets))




