#!/usr/bin/python
# -*- coding: utf-8 -*-
# dnn.py
# described by Kazushi Yamashina
import math
import myerror
import unit
import utility
import connection
# parameter is expressed below
# {numOfUnits:[], weights:[[], ...], means:[], sds: []}
class DNN(object):
	def __init__(self, param):
		# check parameter
		if param == None:
			raise myerror.MyError("NUll parameter")
		if ('numOfUnits' in param) == False:
			raise myerror.MyError("numOfUnits must be specified")
		if len(param['numOfUnits']) <= 2:
			raise myerror.MyError("At least 1 hidden units must be specified")

		# default weight
		self.DEFAULT_WEIGHT = 0
		# number of units
		self.numOfUnits = param['numOfUnits']
		# learning coefficient
		self.learningCoefficient = 0.01
		# mini batch size
		self.miniBatchSize = 10
		# connection objects
		self.connections = {}
		# unit objects
		self.units = {}
		# average of input value
		self.inputMeans = []
		if 'means' in param:
			self.inputMeans = param['means']
		# standard deviation of inputs value
		self.inputSDs = []
		if 'sds' in param:
			self.inputSDs = param['sds']

		# initialize all of processes

		# all layers
		layerArray = []

		# initialize input layer
		# lead is BIAS unit
		inputUnitArray = []

		inputUnitArray.append(unit.Unit(unit.UnitType['BIAS']))
		for i in xrange(0,self.numOfUnits[0]):

			inputUnitArray.append(unit.Unit(unit.UnitType['INPUT']))

		layerArray.append(inputUnitArray)
		# initialize hidden layers
		# lead is BIAS unit
		for j in xrange(1,(len(self.numOfUnits)-1)):
			hiddenUnitArray = []
			hiddenUnitArray.append(unit.Unit(unit.UnitType['BIAS']))
			for k in xrange(0, self.numOfUnits[j]):
				hiddenUnitArray.append(unit.Unit(unit.UnitType['HIDDEN']))

			layerArray.append(hiddenUnitArray)
		# initialize output layer
		outputUnitArray = []
		for l in xrange(0,self.numOfUnits[len(self.numOfUnits)-1]):
			outputUnitArray.append(unit.Unit(unit.UnitType['OUTPUT']))

		layerArray.append(outputUnitArray)

		# unit objects
		self.units = layerArray


		# utility
		dnnUtil = utility.Util()

		# generation of connections
		allConnectionArray = []
		for m in xrange(0,(len(self.numOfUnits)-1)):
			connectionArray = []

			for n in xrange(0,len(self.units[m])):
				connArray = []
				leftUnit = self.units[m][n]

				for p in xrange(0,len(self.units[m + 1])):

					rightUnit = self.units[m + 1][p]

					if rightUnit.getUnitType() != unit.UnitType['BIAS']:
						conn = connection.Connection()
						conn.setRightUnit(rightUnit)
						conn.setLeftUnit(leftUnit)

						if leftUnit.getUnitType() == unit.UnitType['BIAS']:
							conn.setWeight(self.DEFAULT_WEIGHT)
						else:
							conn.setWeight(self.DEFAULT_WEIGHT + dnnUtil.rnorm(0,1))
						connArray.append(conn)

						connTmpArray = rightUnit.getLeftConnections()
						connTmpArray.append(conn)
						rightUnit.setLeftConnections(connTmpArray)

				connectionArray.append(connArray)

				leftUnit.setRightConnections(connArray)

			allConnectionArray.append(connectionArray)

		self.connections = allConnectionArray

		if 'weights' in param:
			for s in xrange(0,len(self.connections)):
				for t in xrange(0,len(self.connections[s])):
					for u in xrange(0,len(self.connections[s][t])):
						self.connections[s][t][u].setWeight(param['weights'][s][t][u])

	def setLearningCoefficient(self, coefficient):
		self.learningCoefficient = coefficient

	def setMiniBatchSize(self, size):
		self.miniBatchSize = size

	def getModel(self):
		weights = []
		for i in xrange(0,len(self.connections)):
			weightsSub = []
			for j in xrange(0,len(self.connections[i])):
				weightsSubSub = []
				for k in xrange(0,len(self.connections[i][j])):
					weightsSubSub.append(self.connections[i][j][k].getWeight())

				weightsSub.append(weightsSubSub)

			weights.append(weightsSub)

		return {'numOfUnits': self.numOfUnits,
				'weights': weights,
				'means': self.inputMeans,
				'sds': self.inputSDs}

	def train(self,  dataSet):
		dnnUtil = utility.Util()
		msd = dnnUtil.getMeanAndSD(dataSet)

		self.inputMeans = msd['means']
		self.inputSDs = msd['sds']

		data = dnnUtil.randomChoice(dataSet, self.miniBatchSize)
		for n in xrange(0,len(data)):

			self.predict(data[n]['data'])

			# for k in xrange(0,(len(self.numOfUnits)-1)):
			k = len(self.numOfUnits)-1
			while  k > 0:
				for l in xrange(0,len(self.units[k])):
					unit_ = self.units[k][l]
					delta = 0
					if (unit_.getUnitType() == unit.UnitType['OUTPUT'] or 
						unit_.getUnitType() == unit.UnitType['HIDDEN']):
						if unit_.getUnitType() == unit.UnitType['OUTPUT']:
							delta = unit_.getOutput()

							if int(data[n]['expected']) == l:
								delta = delta - 1
						else:
							inputValue = unit_.getInput()
							rightConns = unit_.getRightConnections()

							for m in xrange(0,len(rightConns)):
								delta = float(delta) + float(rightConns[m].getRightUnit().getDelta() * rightConns[m].getWeight() * (0 if inputValue < 0 else 1))
						unit_.setDelta(delta)

						conns = unit_.getLeftConnections()

						for p in xrange(0,len(conns)):
							diff = conns[p].getWeightDiff()

							diff += delta * conns[p].getLeftUnit().getOutput()
							conns[p].setWeightDiff(diff)
				k = k - 1
			for q in xrange(0,len(self.connections)):
				for r in xrange(0,len(self.connections[q])):
					for s in xrange(0,len(self.connections[q][r])):
						conn = self.connections[q][r][s]
						weight = conn.getWeight()
						weight -= self.learningCoefficient * conn.getWeightDiff()

						conn.setWeight(weight)

						conn.setWeightDiff(0)

	def test(self, dataSet):
		e = 0

		dnnUtil = utility.Util()
		data = dnnUtil.randomChoice(dataSet, self.miniBatchSize)

		for n in xrange(0,len(data)):
			self.predict(data[n]['data'])

			outputUnits = self.units[len(self.numOfUnits)-1]

			sum = 0

			for i in xrange(0,len(outputUnits)):
				if data[n]['expected'] == i:
					sum = math.log(outputUnits[i].getOutput())

			e += -1 * sum

		avg_e = e / len(data)

		return avg_e

	def predict(self, dataSet):
		demon = 0
		demonArray = []

		dnnUtil = utility.Util()
		data = dnnUtil.normalize(dataSet, self.inputMeans, self.inputSDs)
		g = 0
		for h in xrange(0, len(self.units[0])):
			if self.units[0][h].getUnitType() != unit.UnitType['BIAS']:
				self.units[0][h].setInput(data[g])
				self.units[0][h].setOutput(data[g])
				g = g + 1

		for i in xrange(1, len(self.units)):
			for j in xrange(0, len(self.units[i])):
				unit_ = self.units[i][j]

				if (unit_.getUnitType() == unit.UnitType['HIDDEN'] or
					unit_.getUnitType() == unit.UnitType['OUTPUT']):

					sum = 0

					connArray = unit_.getLeftConnections()

					for k in xrange(0, len(connArray)):
						conn = connArray[k]

						sum = float(sum) + float(conn.getLeftUnit().getOutput() * conn.getWeight())

					unit_.setInput(sum)

					if unit_.getUnitType() == unit.UnitType['OUTPUT']:
						ex = math.exp(unit_.getInput())
						demon += ex
						demonArray.append(ex)

					else:
						if unit_.getInput() < 0:
							unit_.setOutput(0)
						else:
							unit_.setOutput(unit_.getInput())

		result = []
		outputUnits = self.units[len(self.numOfUnits)-1]

		for p in xrange(0, len(demonArray)):
			res = float(demonArray[p] / demon)
			result.append(res)
			outputUnits[p].setOutput(res)

		best = -1
		idx = -1

		for q in xrange(0, len(result)):
			if best < result[q]:
				best = result[q]
				idx = q

		return {'best': idx, 'result': result}

if __name__ == '__main__':
	param = {'numOfUnits':[4, 4, 4, 3]}
	test = DNN(param)







