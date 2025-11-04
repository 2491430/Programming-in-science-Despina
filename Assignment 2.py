# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    numbers = list(set(numbers)) # Duplicates are removed.
    numbers.sort()               # Number are sorted from smallest to biggest.
    return (numbers)
print (remove_duplicates_and_sort([1,1,1,3,4,5,2,2,4,5,1]))

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num        # Adds the next number in the list to the total.
        result.append(total)    # Puts the results next to each other in the list.
    return result
print(cumulative_sum([1,2,3,4,5]))

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[step-1::step]    # Starts at 2nd element (3) and takes every third element after that.
print(slice_every_nth([1,2,3,4,5,6,7,8,9],3))

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):    # Makes sure both lists are the same length.
        return 0
    else:
        return sum(x * y for x,y in zip(list1, list2))    # Pairs up corresponding elements, mulitplies them and then adds their results to form the dot product.
print(dot_product([1,2,3],[4,5,6]))


# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows_1 = len(matrix1)
    columns_1 = len(matrix1[0])
    rows_2 = len(matrix2)
    columns_2 = len(matrix2[0])

    if columns_1 != rows_2: # For multiplication to happen, the number of columns in matrix1 has to equal to the number of rows in matrix2
        print ("Error")

    result = [[0,0],[0,0]]    # Starts matrix off with zeros and then gets filled up

    for i in range (rows_1):
        for j in range (columns_2):
            for k in range (columns_2):                         # i and j for loops go element by element and k for loop calculates product at each position
                result [i][j] += matrix1[i][k] * matrix2[k][j]  # Takes the ith row and kth column in A and multiplies it with kth row and jth column in B.

                                                                # Adds result to existing value
    return result
print(matrix_multiplication([[1, 2], [3,4]], [[5, 6], [7, 8]]))