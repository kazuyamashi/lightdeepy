#!/usr/bin/python
# -*- coding: utf-8 -*-
# connection.py
# described by Kazushi Yamashina

class Connection(object):
	def __init__(self):
		self.leftUnit = {}
		self.rightUnit = {}
		self.weight = 1
		self.weightDiff = 0

	def setLeftUnit(self, unit):
		self.leftUnit = unit

	def setRightUnit(self, unit):
		self.rightUnit = unit

	def getLeftUnit(self):
		return self.leftUnit

	def getRightUnit(self):
		return self.rightUnit

	def setWeight(self, weight):
		self.weight = weight

	def getWeight(self):
		return self.weight

	def setWeightDiff(self, diff):
		self.weightDiff = diff

	def getWeightDiff(self):
		return self.weightDiff
