# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    list = [num1, num2, num3]
    return (max(list))                    # The built-in fuction max takes three numbers and returns the largest of them

num1 = int(input("Enter a number: "))     # Takes three numbers from the user
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print ({built_in_functions_max(num1, num2, num3)})

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    list = [num1, num2, num3]
    return (min(list))                     # The built-in function min returns the smallest number inputed 

num1 = int(input("Enter a number: "))      # Takes three numbers from the user
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print ({built_in_functions_min(num1, num2, num3)})

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:              # If the number is positive, the function returns positive or else retruns negative or zero
        return "Postive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter a number: "))
print ({check_number(number)})

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    for i in range (1, rows+1):     # The function loops from 1 until rows
        print ('*' * i)             # Prints i stars in each line 

rows = int(input("Enter a number of rows: "))
star_shape(rows)

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    count = 1
    while count <= limit:
        if count % 3 == 0:
            print ("Multiple of 3")     # Replaces if divisible by 3 
        else:
            print (count)               # Otherwise prints the number until limit
        count += 1
        
limit = int(input("Enter the limit: "))
count_multiples_of_3(limit)

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    for num in range (start, end+1):
        if num % 2 == 0:                  
            total += num              # If even number, adds number to total until the end 
    return total

start = int(input("Enter a number for the start: "))
end = int(input("Enter a number for the end: "))
print (f"The sum of even numbers in a given range is: {sum_of_even_numbers(start, end)}")