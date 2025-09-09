# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g=9.8
    result= h0-1/2*g*t*t
    return result  

height= (float(input("Enter the height:")))
time= (float(input("Enter the time:")))
print (f"Height of the ball?", {calculate_height(height,time)})
height= (float(input("Enter the height:")))
time= (float(input("Enter the time:")))
print (f"Height of the ball?", {calculate_height(height,time)})
height= (float(input("Enter the height:")))
time= (float(input("Enter the time:")))
print (f"Height of the ball?", {calculate_height(height,time)})


# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    speed= 20
    result=speed*time 
    return result

time= (float(input("Enter the time")))
print(f"The car will travel", {calculate_car_distance(time)})
time= (float(input("Enter the time")))
print(f"The car will travel", {calculate_car_distance(time)})
time= (float(input("Enter the time")))
print(f"The car will travel", {calculate_car_distance(time)})

