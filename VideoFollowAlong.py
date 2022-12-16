import numpy as np

np.random.seed(0)

#(between 0 and 1)
#X = random.randint(0, 1)
#np.random.randint(1, size=(1,2), dtype=’l’)
X = [[1, 2, 3, 2.5],
         [2.0, 5.0, -1.0, 2.0],
         [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weight = np.random.randn(n_inputs, n_neurons)
    def forward(self):
        pass

print(0.10*np.random.randn(4,3))