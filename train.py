import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

class train(object):
	
	def __init__(self,features,labels):
		self.features = features
		self.labels = labels


	def getSVM(self):
		clf = svm.SVC(kernel = "rbf",gamma = 0.001,C = 100)
		clf.fit(np.array(self.features),np.array(self.labels))
		return clf

	def getGaussianNB(self):
		clf  = GaussianNB()
		clf.fit(np.array(self.features),np.array(self.labels))
		return clf

	def getDecisionTree(self):
		clf = tree.DecisionTreeClassifier()
		clf.fit(np.array(self.features),np.array(self.labels))
		return clf

	def getKNN(self):
		clf = KNeighborsClassifier(n_neighbors=15)
		clf.fit(np.array(self.features),np.array(self.labels))
		return clf
