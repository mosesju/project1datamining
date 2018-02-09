import csv
import math

def train(testX,testY,trainingFeature):
	distance = {}
	minDist=1000

	for  k in trainingFeature:
		for l in k:
			#takes values out of Array
			trainX=k[0]
			trainY=k[1]
			label=k[2]
			#calculates distance
			eucDist=math.sqrt((testX-trainX)**2+(testY-trainY)**2)
			#goes through and only puts minimum distances into the array
			if eucDist < minDist:
				minDist=eucDist
				distance.update({minDist:label})


	#calculates minimum distance for each test point

	#minDist = min(distance)
	minVal = min(distance)
	value=distance.get(minVal)
	print(testX, testY, minVal, value)


def main():
	terms = []
	dataObjectCount =0
	testData = []
	trainingData = []
	#opens file and splits into trianing and test data
	with open('fruit_data_with_colors.txt','r') as tsv:
		for line in tsv:
			if dataObjectCount %5 == 0:
				if dataObjectCount != 0:
					testData.append(line.strip().split('\t'))
			else:
				trainingData.append(line.strip().split('\t'))

			dataObjectCount= dataObjectCount + 1

	#parses data
	trainingFeature =[]
	testFeature=[]
	for line in trainingData:
		dataObject = []
		dataObject.append(float(line[5]))
		dataObject.append(float(line[6]))
		dataObject.append(float(line[0]))
		trainingFeature.append(dataObject)

	for line in testData:
		dataObject=[]
		dataObject.append(float(line[5]))
		dataObject.append(float(line[6]))
		testFeature.append(dataObject)


	for i in testFeature:
		for j in i:
			testX=i[0]
			testY=i[1]
			train(testX,testY,trainingFeature)


main()
