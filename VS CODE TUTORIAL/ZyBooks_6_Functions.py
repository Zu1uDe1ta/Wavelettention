

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

#6.5.1: Program that calculates cylinder volume and surface area by calling a modular function for the cylinder's base.

def calc_circular_base_area(radius):
   return math.pi * radius * radius

def calc_cylinder_volume(baseRadius, height):
   return calc_circular_base_area(baseRadius) * height

def calc_cylinder_surface_area(baseRadius, height):
   return (2 * math.pi * baseRadius * height) + (2 * calc_circular_base_area(baseRadius))

radius = float(input('Enter base radius: '))
height = float(input('Enter height: '))

print('Cylinder volume: ' + '{:.3f}'.format(calc_cylinder_volume(radius, height)))
print('Cylinder surface area: ' + '{:.3f}'.format(calc_cylinder_surface_area(radius, height)))


#6.5.2: Function definition: Volume of a pyramid with modular functions.

def calc_base_area(base_length, base_width):
   return base_length * base_width

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    return calc_base_area(base_length, base_width) * pyramid_height * (1/3)
    


# Figure 6.6.1: Using the pass statement in a function stub performs no operation.
length = float(input())
width = float(input())
height = float(input())
print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))


def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet

def steps_to_calories(num_steps):
    pass  

steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print('Feet:', feet)

calories = steps_to_calories(steps)
print('Calories:', calories)

# Figure 6.6.2: A function stub using a print statement.
def steps_to_calories(steps):
    print('FIXME: finish steps_to_calories')
    return -1


# Figure 6.6.3: Stopping the program using NotImplementedError in a function stub.
import math

def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError
        
def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_perimeter_length(points):
    perimeter = side_length(points[0], points[1])
    perimeter += side_length(points[0], points[2])
    perimeter += side_length(points[1], points[2])
    return perimeter

coordinates = get_points(3)
print('Perimeter of triangle:', get_perimeter_length(coordinates))



# 6.6.1: Function stubs: Statistics.
def get_user_num():
    print('FIXME: Finish get_user_num()')
    return -1

def compute_avg(user_num1, user_num2):
    print('FIXME: Finish compute_avg()')
    return -1
    
user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)

