"""
	Main Interfacing Program for all the Applications
"""

from train import train
import numpy as np
from sklearn.metrics import accuracy_score
import plotter
from matplotlib import pyplot as plt

class Gesture(object):

	def __init__(self,project_id):
		# path store the file name where the dataset to be stored
		self.features = []
		self.labels = []

	def initClassifier(self):
		trainer = train(self.features,self.labels)
		self.clf  = trainer.getSVM()
		return self.clf

	def predict(self,feature):
         prediction1=self.clf.decision_function(np.array([feature]))
         print prediction1
         return self.clf.predict([feature])

	def addGesture(self,feature,label):
		self.features.append(feature)
		self.labels.append(label)

	def addDataFromFile(self,path,label):
		x,y,z = plotter.getFeatures(path)
		temp = x + y + z
		self.features.append(temp[:50])
		self.labels.append(label)

	def getIndependentFeature(self,path):
		x,y,z = plotter.getFeatures(path)
		return x,y,z

	def plotImage(self,path):
		x,y,z = self.getIndependentFeature(path)
		img = plotter.buildImg(x,y,z)
		plt.plot(img)
		plt.show()

	def getDataFromFile(self,path):
		x,y,z = plotter.getFeatures(path)
		temp = x + y + z
		return temp[:50]

	def train(self,folders,names,labels):
		for i in range(len(folders)):
			for j in names:
				path = "./dataset/" + folders[i] + "/" + j
				self.addDataFromFile(path,labels[i])
                        #print path

		
