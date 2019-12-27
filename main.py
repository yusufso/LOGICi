import numpy as numpy

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoidDer(x):
    return x * (1 - x)

#linear algebra problem
#trainIn * x = trainOut

trainIn = np.array([[0, 0, 1],
                       [1, 1, 1],
                       [1, 0, 1],
                       [0, 1, 1]])

#transpose into column matrix
trainOut = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

weights = np.random.random((3, 1)) - 1

print("Weights before training: ")
print(weights)

for i in range(30000):
    inLayer = trainIn

    outputs = sigmoid(np.dot(inLayer, weights))

    error = trainOut - outputs

    adjustBy = error * sigmoidDer(outputs)

    weights += np.dot(inLayer.T, adjustBy)

print("Weights after training: ")
print(weights) 


print("Outputs after training: ")
print(outputs)