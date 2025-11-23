import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(numbers, filename = "numbers.txt"):

# Opens file in write mode and writes the numbers

    myfile = open(filename, 'w')
    myfile.write(str(numbers))
    myfile.close()

# Opens the file and reads the contents

    myfile = open(filename,'r')
    print(myfile.read())
    myfile.close()

numbers = [1,2,3,4,5] 
write_and_read_txt(numbers)

 

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(data, filename = "data.csv"):

# Opens file in write mode and writes list of lists

    myfile = open(filename, 'w')
    myfile.write(str(data))
    myfile.close()

# Opens the file and reads the contents

    myfile = open(filename,'r')
    print(myfile.read())
    myfile.close()

data = [[1,2,3] , [4,5,6] , [7,8,9]]
write_and_read_csv(data)

# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    return np.array([])

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):
    plt.plot(numbers, marker='o', linestyle='-')
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Line Plot")
    plt.grid(True)
    plt.show()
    return

numbers = [1,2,3,4,5,6,7,8,9,10]
plot_data(numbers)

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data):
    plt.hist2d(data[:, 0], data[:, 1], bins=50, density=True)
    plt.colorbar(label="Density")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Density Plot")
    plt.show()
    return
          
data = np.random.randn(5000,2)
density_plot(data)