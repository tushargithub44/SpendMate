# importing the required module 
import matplotlib.pyplot as plt 
import random

# x axis values 
x = [1,2,3,4,5,6] 
for i in range(25):
        x.append(i+6)
# corresponding y axis values 
y = [2,0,1,4,0,3] 
for i in range(25):
        y.append(random.randrange(0,5))

# plotting the points 
plt.plot(x, y) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('My first graph!') 

# function to show the plot 
plt.show() 
