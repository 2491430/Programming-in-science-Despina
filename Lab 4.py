# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):

    if day_number <1 or day_number >7: 
        print("It is invalid") 
    elif day_number >= 1 and day_number <= 5:
        print("It is a weekday")
    else:
        print("It is a weekend")

day_number= int(input("What is the number?"))
{check_weekday_or_weekend(day_number)}

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    
    if day_number == 1:
        return "monday"
    elif day_number == 2:
        return "tuesday"
    elif day_number == 3:
        return "wednesday"
    elif day_number == 4:
        return "thursday"
    elif day_number == 5:
        return "friday"
    elif day_number == 6:
        return "saturday"
    elif day_number == 7:
        return "sunday"
    
day_number= int(input("What is the number?"))
print (f"The day of the week is", {get_day_name(day_number)})