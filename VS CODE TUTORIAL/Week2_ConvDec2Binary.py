#   Name: Chris Chavez
#   Date: 14 JULY 2021
#   Class: CMPSC 132
#   Description: Program converts decimal to binary and hex. 

import math 

print('Commonly known as "the way computers talk"\n a binary number is a number expressed in the base-2 \n numeral system or binary numeral system, a method of mathematical\n expression which uses only two symbols: typically "0" and "1". \n')
print('In mathematics and computing, the hexadecimal\n numeral system is a positional numeral system that\n represents numbers using a radix of 16. Unlike the common way of\n representing numbers using 10 symbols, hexadecimal uses 16 distinct\n symbols, most often the symbols "0"–"9" to represent\n values 0 to 9, and "A"–"F" to represent values 10 to 15. \n')
print('This program will will convert a decimal\n input into a binary number and a hexadecimal number.  \n')
num = int(input("Please input an integer/whole\n number number between 0 and 2 Billion: \n"))

# Function checks if the input is between the requested parameters
def check():
  global num
  while True:
    try:
      if num <= 2000000000 and num >= 0:
        return num
        print("You entered the number {}", num)
      print("Invalid value entered.")
    except Exception as e:
      print(e)

# Function to convert decimal number to binary using recursion
def DecimalToBinary(num):
  if num >= 1:
    DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value

     
    # Calling function
    check()
    DecimalToBinary(num)

