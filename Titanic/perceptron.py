import numpy as np

class Perceptron:
    def __init__(self,epoch=1,learning_rate=0.01,bias=0.1):
        self.epochs = epoch
        self.learning_rate = learning_rate
        self.learning_rate_b = bias
        self.w = np.random.rand(10,1)
        self.b = np.random.rand(1,1)

    def fit(self,x_train,y_train):
        x_train = np.matrix(x_train)
        for epoch in range(1):
            for i in range(x_train.shape[0]):
                predict_train = np.matmul(x_train[i],self.w) + self.b
                error = y_train[i] - predict_train
                self.w += x_train[i].T  * error * self.learning_rate 
                self.b += self.learning_rate * error
    
    def predict(self,x_test):
        y_pred = np.matmul(x_test,self.w) + self.b
        y_pred = np.where(y_pred>0.5,1,0)
        return y_pred