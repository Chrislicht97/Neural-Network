import numpy as np

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

#(between -1 and 1)
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87],
           [0.3, 0.5, -0.34, -0.5]]


#output = np.dot(inputs, np.array(weights).T) + biases
output = np.dot(X, weights)
print(output)