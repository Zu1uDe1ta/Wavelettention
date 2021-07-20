

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

# Figure 6.7.1: Function example: Determining fees given an item selling price for an auction website.
def calc_ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and 
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('Ebay fee: $', calc_ebay_fee(selling_price))


#6.7.1: Output of functions with branches/loops.
def compute(numbers):
    result = 1
    for num in numbers:
        result *= num - 3
    return result

values = [7, 5, 6]
computed_value = compute(values)
print(computed_value)

#
def get_numbers():
    user_input = input()
    values = []
    for token in user_input.split():
        values.append(int(token))
    return values

def print_selected_numbers():
    numbers = get_numbers()
    for number in numbers:
        if number < 5:
            print(number)

print_selected_numbers()


# 6.7.2: Function with branch: Popcorn.

def print_popcorn_time(bag_ounces):
    bag_ounces = int(bag_ounces)
    if bag_ounces < 3: 
        print("Too small")
    elif bag_ounces > 10: 
        print("Too large")
    else: 
        print(str(6 * bag_ounces) + " seconds")
    

user_ounces = int(input())
print_popcorn_time(user_ounces)




# 6.9.1: Function errors: Copying one function to create another.

def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0
    
    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 10.0
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

value_k = float(input())
print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')


# 6.12.1: Change order of elements in function list argument.
def swap(values_list): 
    values_list[0], values_list[-1] = values_list[-1], values_list[0]
    return values_list

values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
