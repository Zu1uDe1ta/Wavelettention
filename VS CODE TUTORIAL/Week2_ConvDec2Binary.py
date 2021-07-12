#   Name: Chris Chavez
#   Date: 14 JULY 2021
#   Class: CMPSC 132
#   Description: Program converts decimal to binary and hex. 

import math 



print('Commonly known as "the way computers talk" a binary number is a number expressed in the base-2 \n numeral system or binary numeral system, a method of mathematical expression which uses only two symbols: typically "0" and "1". \n')
print('In mathematics and computing, the hexadecimal numeral system is a positional numeral system that\n represents numbers using a radix of 16. Unlike the common way of representing numbers using 10 symbols, hexadecimal uses 16 distinct\n symbols, most often the symbols "0"–"9" to represent values 0 to 9, and "A"–"F" to represent values 10 to 15. \n')
print('This program will will convert a decimal input into a binary number and a hexadecimal number.  \n')

# Function checks if the input is between the requested parameters
def check():
  while True:
    try:
      num = int(input("Please input an integer/whole number number between 0 and 2 Billion: \n"))
      if num <= 2000000000 and num >= 0:
        break
      print("Invalid value entered.")
    except Exception as e:
      print(e)

check()
  

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 24
     
    # Calling function
    DecimalToBinary(dec_val)




"""
def equationroots(): 
answer = 0
3 while len(number) > 0:                  #do next 3 lines until length of number is 0
4     answer = answer * 2                 #multiply answer by 2
5     answer = answer + int(number[0])    #add leftmost digit to answer
6     number = number[1:]                 #remove leftmost digit
"""



    global a, b, c
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
        print("\nreal and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print("\nreal and same roots") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("\nComplex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 

"""" 
# Driver Program 
a = 2
b = -10
c = 0
"""

# If a is 0, then incorrect equation
if a == 0: 
        print("\nInput correct quadratic equation") 
  
else:
    equationroots()

