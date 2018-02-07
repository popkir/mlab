import pandas
import numpy as np
import matplotlib.pyplot as plt

class Logistic():

    def __init__(self):
        self.weights = None #TODO: write
        self.biases = None #TODO: write
        pass

    def logistic(self, z):
        pass

    def get_data(self):
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        self.dataset = pandas.read_csv(url, names=names)

    def get_sample(self, size):
        #Get some number of samples from the dataset, turn them into vectors you can feed into the equations. 
        pass    

    def fit_SGD(self, batch_size):
        pass

    def fit_BGD(self):
        #Use all the data, don't split into minibatches
        pass

    def predict(self, inputs):
        pass

    def plot(self):
