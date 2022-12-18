import numpy as np
import random

#empty list
list1 = list() 
sizes = ("small", "medium", "large")
yesno = ("yes", "no")

#Choices are small, medium, or large.
size = input("Do you want small, medium, or large network?").lower()
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

fLoop = input("Do you want a feedback loop? Y/N").lower()
if fLoop == "yes" or "y":
    fLoops = input("How many loops would you like?")
elif fLoop == "no" or "n":
    pass
else:
    print("Sorry, that's not a valid input.")


X = list1
#X += np.random.randint(1, size=(1,2))
#X += random.randint(0, 1)

#(Weights fall between -1 and 1)
weights = random.uniform(-1, 1)

output = np.dot(X, weights)
print(output)