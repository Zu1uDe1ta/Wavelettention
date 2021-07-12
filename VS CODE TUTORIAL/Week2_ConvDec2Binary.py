#   Name: Chris Chavez
#   Date: 14 JULY 2021
#   Class: CMPSC 132
#   Description: Program converts decimal to binary and hex. 

import math 

print('Commonly known as "the way computers talk"\n a binary number is a number expressed in the base-2 \n numeral system or binary numeral system, a method of mathematical\n expression which uses only two symbols: typically "0" and "1". \n')
print('In mathematics and computing, the hexadecimal\n numeral system is a positional numeral system that\n represents numbers using a radix of 16. Unlike the common way of\n representing numbers using 10 symbols, hexadecimal uses 16 distinct\n symbols, most often the symbols "0"–"9" to represent\n values 0 to 9, and "A"–"F" to represent values 10 to 15. \n')
print('This program will will convert a decimal\n input into a binary number and a hexadecimal number.  \n')
num = int(input("Please input an integer/whole\nnumber between 0 and 2 Billion: \n"))

# Function checks if the input is between the requested parameters
def check(num):
  while True:
    try:
      if num <= 2000000000 and num >= 0:
        print("\nYou entered the number", num, "\nin binary that is: ")
        # print("in binary that is")
        return num
      print("Invalid value entered.")
    except Exception as e:
      print(e)

# Function to convert decimal number to binary using recursion
def DecimalToBinary(num):
  if num >= 1:
    DecimalToBinary(num // 2)
    print(num % 2, end = '')

# Function to convert decimal number to hexdecimal 
def DecimalToHeximal(num):
  conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
  hexadecimal = ''
  while(num>0):
    remainder = num%16
    hexadecimal = conversion_table[remainder]+ hexadecimal
    num = num//16
  print("\nand in hexadecimal:", hexadecimal)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling function
    check(num)
    DecimalToBinary(num)
    DecimalToHeximal(num)

