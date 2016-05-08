#!/usr/bin/python
# -*- coding: utf-8 -*-
# utility.py
# described by Kazushi Yamashina

import random
import math

# utility function
class Util(object):

	# normal random number
	def rnorm(self, mean, sd):
		x = random.random()
		y = random.random()
		ret = mean + sd * math.sqrt(-2 * math.log(x)) * math.cos(2 * math.pi * y)
		return ret

	# choice the number randomly from input array
	def randomChoice(self, ary, count):
		if len(ary) <= count:
			return ary
		# new array
		newAry = []
		# used index
		used = {}

		while True:
			r = int(math.floor(random.random() * len(ary)))

			if r in used:
				continue

			newAry.append(ary[r])

			if len(newAry) == count:
				break

			used[r] = 1
		return newAry

	def getMeanAndSD(self, dataSet):
		sum = []
		# summation
		for i in xrange(0,len(dataSet)):
			items = dataSet[i]['data']
			# for j in xrange(0,len(items)):
			# 	sum[i] += items[j]
			for j in xrange(0,len(items)):
				if len(sum) < len(items):
					sum.append(0)
				sum[j] += items[j]
		means = []
		# average
		for k in xrange(0,len(sum)):
			means.append(0)
			means[k] = float(sum[k]) / len(dataSet)
		# sum of the squared difference
		squaredSum = []
		for l in xrange(0,len(dataSet)):
			items2 = dataSet[l]['data']
			for m in xrange(0,len(items2)):
				if len(squaredSum) < len(items2):
					squaredSum.append(0)
				squaredSum[m] += math.pow((items2[m] - means[m]), 2)
		# standard deviation
		sds = []
		for p in xrange(0,len(dataSet)):
			items3 = dataSet[p]['data']
			for q in xrange(0,len(items3)):
				if len(sds) < len(items3):
					sds.append("")
				sd = math.sqrt(squaredSum[q] / len(dataSet))
				sds[q] = sd

		return {"means": means, "sds": sds}

	def normalize(self, dataAry, means, sd):
		newAry = []
		for i in xrange(0,len(dataAry)):
			newAry.append(float(dataAry[i] - means[i]) / sd[i])
		return newAry

if __name__ == '__main__':
	pass