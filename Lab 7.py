

# Function 1: Rotate the Array
# This function creates an array of a specified size, fills it with numbers starting from `starting_integer` and increasing by 3,
# then rotates elements at even indices 2 positions to the left.
def rotate_the_array(array_size, starting_integer):
  # initialize an array of array_size with all zeros
   the_array = [0] * array_size
  # use for i in range (....) to add value for each element of the the_array[i]
  # loop it so it takes starting_integer as the first index of the_array and then keep adding 3 to the next index of  the_array
   for i in range(array_size -1, -1, -1):
      the_array[i] = starting_integer
      starting_integer += 3


   
   #Testing
   print("Original array: ", the_array)
   print(the_array[0])
   
   for i in range(0, array_size - 2, 2):
      temp = the_array[i]
      the_array[i] = the_array[i + 2]
      the_array[i + 2] = temp
   
   # Testing
   print("Rotated array: ", the_array)
   
   return the_array
rotate_the_array(6, 2)