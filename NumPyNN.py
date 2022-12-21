import numpy as np
import random

#empty list
input_layer = list()
weights = list()
output_layer = list()

#Choices are small, medium, or large.
size = input("Do you want small, medium, or large network?").lower()
if size in ["small", "medium", "large"]:
    numinputs = 2 if size == "small" else 3 if size == "medium" else 4
    numweights = 4 if size == "small" else 6 if size == "medium" else 8
    numoutputs = 2 if size == "small" else 3 if size == "medium" else 4
else:
    print("Sorry, that's not a valid input.")

#Iterating till user's range is reached.
for i in range(int(numinputs)):
    #Asking for input of 1 value.
    n = input("Enter a value:")
    #Adding that value to the list.
    input_layer.append(int(n))

#Generating weights.
for i in range(int(numweights)):
    #(Weights fall between -1 and 1)
    weights.append(random.uniform(-1, 1))

#fLoop
feedback_loop = input("Do you want a feedback loop? Y/N").lower()
#Choices are Y/N.
if feedback_loop == "yes" or "y":
    loop_rounds = int(input("How many loops would you like?"))
elif feedback_loop == "no" or "n":
    pass
else:
    print("Sorry, that's not a valid input.")

for i in range(int(loop_rounds)):
    np.dot(input_layer, weights)

#X += random.randint(0, 1)

output = max(output_layer)
print(output)