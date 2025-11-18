import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):
    return []
 

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):
    return []

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