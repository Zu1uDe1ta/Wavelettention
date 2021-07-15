

# 6.2.1: Print functions.
def print_points(name, age, total_points):
    print('{} is {}'.format(name, age))
    print('{} made {} points'.format(name, total_points))

user_name = 'Sam'
user_age = 22
regular_time_points = 22
overtime_points = 5

print_points(user_name, user_age, regular_time_points + overtime_points)

# 6.2.2: Function call with parameter: Printing formatted measurement.
def print_feet_inch_short(num_feet, num_inches):
    print('{}\' {}"'.format(num_feet, num_inches))
    
user_feet = int(input())
user_inches = int(input())

print_feet_inch_short(user_feet, user_inches) # Will be run with (5, 8), then (4, 11)

#6.4.1: Functions: Factoring out a unit-conversion calculation.
def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled): 
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled


#6.5.1: Function call in expression.
def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)


print('max_sum is:', max_sum)