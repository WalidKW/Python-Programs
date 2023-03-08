import numpy as np

def H(x, w):
    rows = x.shape[0] # number of features
    print("Number of features =", rows)
    cols = x.shape[1] # number of samples
    print("Number of samples =", cols)
    hypothesis = np.dot(w.T, x) # calculate hypothesis
    print("Hypothesis =", hypothesis)
    return hypothesis

def Sigmoid(hypothesis):
    return 1/(1+np.exp(-hypothesis))

def predict(logits):
    return np.where(logits>=0.5, 1, 0)

# input values
w = np.array([[-24],[ 0.2],[ 0.2]])
x = np.array([[1,1,1,1,1],
              [30,35,60,97,40],
              [43,72,86,80,30]])

# calculate hypothesis
hypothesis = H(x, w)


# calculate sigmoid value
sigmoid_value = Sigmoid(hypothesis)
print("Sigmoid value:", sigmoid_value)

# make prediction
prediction = predict(sigmoid_value)
print("The prediction is:", prediction)

# calculate number of misclassifications
true_labels = np.array([0,1,1,1,0])
misclassified = np.sum(np.abs(prediction - true_labels))
print(f"Number of misclassifications is {misclassified} sample/s")
