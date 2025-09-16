import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
    
    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians(theta))
    return (round (x,5), round(y,5))

r=float(input("What is the value of r?"))
theta= float(input("What is the value of theta?"))
print(f"The coordinates are:", {polar_to_cartesian(r,theta)})

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r=math.sqrt(x**2 + y**2)
    theta=math.degrees(math.atan(y/x))
    return (round(r,5), round (theta,5))

x=float(input("What  is the x value?"))
y=float(input("What is the y value?"))
print(f"The coordinates are:", {cartesian_to_polar(x,y)})

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    x_t=A*math.cos(2*math.pi*f*t+ math.radians(phi))
    return x_t

A= float(input("What is the value of A?"))
f= float (input("What is the value of the frequency?"))
phi= float (input ("What is the value of phi?"))
t= float(input("What is the value of t?"))
print(f"The position is:", {pendulum_position(A, f, phi, t)})