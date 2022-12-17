import numpy as np
import random

#empty list
list1 = list() 
sizes = ("small", "medium", "large")

#Choices are small, medium, or large.
size = input("Do you want small, medium, or large network?")
if size in sizes:
    inputs = 2 if size == "small" else 3 if size == "medium" else 4
else:
    print("Sorry, that's not a valid input.")

#Iterating till user's range is reached.
for i in range(int(inputs)):
    #Asking for input of 1 value.
    n = input("Enter a value:")
    #Adding that value to the list
    list1.append(int(n))


X = list1
#X = np.random.randint(1, size=(1,2))
#X = random.randint(0, 1)

#(Weights fall between -1 and 1)
weights = random.uniform(-1, 1)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = weights * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

#output = np.dot(inputs, np.array(weights).T) + biases
output = np.dot(X, weights)
print(output)