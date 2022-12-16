import numpy as np

#(between 0 and 1)
inputs = [[0.2, 0, 0.6, 0.8],
         [0.3, 0.6, 0.9, 0.2],
         [0.5, 0.7, 0.3, 0.6],
         [1, 0.4, 0.3, 0.7]]
#(between -1 and 1)
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87],
           [0.3, 0.5, -0.34, -0.5]]

#Use bias to make it look better or sum
#biases = [3, 2, 0.5, 4]

#output = np.dot(inputs, np.array(weights).T) + biases
output = np.dot(inputs, weights)
print(output)