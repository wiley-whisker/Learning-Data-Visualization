import matplotlib.pyplot as plt

input_vals = [1,2,3,4,5] # we will use these to set the coresponding x component.
squares = [1, 4, 9, 16, 25] # could just use this and it will plot it where x = index and y = squares[index] old way


#plt.plot(squares, linewidth=3) old way
plt.plot(input_vals, squares, linewidth=3) # new way

#set chart title and label axis
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=4)
plt.ylabel("Square of value", fontsize=4)

# set the tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()