import numpy as np

#(between 0 and 1)
inputs = [1,2,3,2.5]
#(between -1 and 1)
weights = [0.2,0.8,-0.5,1.0]
#Are we using bias?
biases = [3, 2, 0.5]

output = np.dot(weights, inputs) + biases
print(output)