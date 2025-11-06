import numpy as np

# Function 1: Read values from a file into an array
# This function reads numerical values from a text file and stores them in a NumPy array.
def read_values_from_file(filename):
    with open(filename,'r') as file:
        values = [float(line.strip()) for line in file]
    return np.array(values)
arr= read_values_from_file(r"C:\Users\2491430\Downloads\values.txt")
print (arr)

# Function 2: Read Oscillatory Wave Data and Compute Statistics
# This function reads a file containing wave data with length and amplitude values into a NumPy array.
# It also computes the mean and maximum amplitude.
def read_oscillatory_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    lengths = data[:,0]
    amplitudes = data[:, 1]
    mean_amplitude = np.mean(amplitudes)
    max_amplitude = np.max(amplitudes)
    return data, mean_amplitude, max_amplitude
data, mean_amp, max_amp = read_oscillatory_wave_data(r"C:\Users\2491430\Downloads\wave_data.csv")

print ("Mean amplitude:", mean_amp)
print ("Max amplitude: ", max_amp)

# Function 3: Read Standing Wave Data and Compute Wave Speed
# This function reads a file containing standing wave data with length and tension values into a NumPy array.
# It also computes the wave speed using v = sqrt(T/μ), where μ = mass per unit length (assumed to be 1 for simplicity).
def read_standing_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    lengths = data[:, 0]
    tensions = data [:, 1]
    wave_speeds = np.sqrt(tensions / lengths)
    return data, wave_speeds
data, wave_speeds = read_standing_wave_data(r"C:\Users\2491430\Downloads\standing_wave.csv")
print ("Wave speed: ", wave_speeds)