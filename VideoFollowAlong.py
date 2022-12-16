import numpy as np

#(between 0 and 1)
inputs = [1,2,3,2.5]

#(between -1 and 1)
weights = [[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]

#Use bias to make it look better or sum
biases = [3, 2, 0.5]

#output = np.dot(inputs, np.array(weights).T) + biases
output = np.dot(inputs, np.array(weights).T) + biases
print(output)