#!/usr/bin/python
# -*- coding: utf-8 -*-
# unit.py
# described by Kazushi Yamashina
import myerror

UnitType ={
		'INPUT': 0,
		'HIDDEN': 1,
		'BIAS': 2,
		'OUTPUT': 3}

class Unit(object):

	def __init__(self, unitType):

		self.unitType = unitType

		self.leftConnections = []
		self.rightConnections = []

		self.inputValue = 0
		self.outputValue = 0

		if unitType == UnitType["BIAS"]:
			self.outputValue = 1

		self.delta = 0

	def getUnitType(self):
		return self.unitType

	def setLeftConnections(self, connections):
		if (self.unitType != UnitType['HIDDEN'] and 
			self.unitType != UnitType['OUTPUT']):
			raise myerror.MyError("Invalid unit type!")
		self.leftConnections = connections

	def setRightConnections(self, connections):
		if (self.unitType != UnitType['INPUT'] and 
			self.unitType != UnitType['HIDDEN'] and 
			self.unitType != UnitType['BIAS']):
			raise myerror.MyError("Invalid unit type!")
		self.rightConnections = connections

	def getLeftConnections(self):
		if (self.unitType != UnitType['HIDDEN'] and
			self.unitType != UnitType['OUTPUT']):
			raise myerror.MyError("Invalid unit type!")
		return self.leftConnections

	def getRightConnections(self):
		if (self.unitType != UnitType['INPUT'] and 
			self.unitType != UnitType['HIDDEN'] and 
			self.unitType != UnitType['BIAS']):
			raise myerror.MyError("Invalid unit type!")
		return self.rightConnections

	def setInput(self,value):
		if (self.unitType != UnitType['INPUT'] and 
			self.unitType != UnitType['HIDDEN'] and 
			self.unitType != UnitType['OUTPUT']):
			raise myerror.MyError("Invalid unit type!")
		self.inputValue = value

	def getInput(self):
		if (self.unitType != UnitType['INPUT'] and 
			self.unitType != UnitType['HIDDEN'] and 
			self.unitType != UnitType['OUTPUT']):
			raise myerror.MyError("Invalid unit type!")
		return self.inputValue

	def setOutput(self, value):
		self.outputValue = value

	def getOutput(self):
		return self.outputValue

	def setDelta(self, delta):
		if (self.unitType != UnitType['HIDDEN'] and
			self.unitType != UnitType['OUTPUT']):
			raise myerror.MyError("Invalid unit type!")
		self.delta = delta

	def getDelta(self):
		if (self.unitType != UnitType['HIDDEN'] and
			self.unitType != UnitType['OUTPUT']):
				raise myerror.MyError("Invalid unit type!")
		return self.delta

if __name__ == '__main__':
	pass