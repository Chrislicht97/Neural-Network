import numpy as np
import random

#empty list
input_layer = list()
weights = list()
products = list()
sizes = ("small", "medium", "large")

#Choices are small, medium, or large.
size = input("Do you want small, medium, or large network?").lower()
if size in sizes:
    inputs = 2 if size == "small" else 3 if size == "medium" else 4
    numweights = 4 if size == "small" else 6 if size == "medium" else 8
    outputs = 2 if size == "small" else 3 if size == "medium" else 4
else:
    print("Sorry, that's not a valid input.")

#Iterating till user's range is reached.
for i in range(int(inputs)):
    #Asking for input of 1 value.
    n = input("Enter a value:")
    #Adding that value to the list.
    input_layer.append(int(n))

#Generating weights.
for i in range(int(numweights)):
    #(Weights fall between -1 and 1)
    weights.append(random.uniform(-1, 1))

#Choices are Y/N.
fLoop = input("Do you want a feedback loop? Y/N").lower()
if fLoop == "yes" or "y":
    fLoops = int(input("How many loops would you like?"))
elif fLoop == "no" or "n":
    pass
else:
    print("Sorry, that's not a valid input.")

for i in range(int(fLoops)):
    np.dot(input_layer, weights)

        
#X += random.randint(0, 1)

output = np.dot(input_list, weights)
print(output)