# 20demo.py by david_berrios

print ("hello, again") # greeting

# addition

print (1+1)

#subtraction

print (1-1)

#multiplication

print (2 * 2)

#division

print (1/2)

#exponentiation

print (2 ** 3)

#integer divide

print (5 // 2)

#remainder

print (5 % 2)

#precedence

print (5 * (2+1))

#imported math functions

import math

print ('hello again')

print (1.5e-2)

print (1+1)

print (2 ** 3)

print (pow (2,3))

print (math.pow(2,3))

print (2 ** 0.5)

print (math.sqrt (2))

print (math.log(2))

#using variables to do math

a = 3 							#side of triangle
b = 4							#side of triangle
c = math.sqrt(a**2 + b**2)		#hypotenuse
print(c)

print(type (a), type(b), type (c), sep=', ')

#Creating a pythagorean formula function

def pythagoras (a, b):
	c = math.sqrt(a**2 + b**2)
	return c
x = pythagoras (3, 4)
print (x)

#Omitting variables c and x from pythagorean formula function

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print (pythagoras (3,4))
print (pythagoras (1,1))

#Using assert function 

#def pythagoras(a, b):
	#assert(a > 0)
	#assert(b > 0)
	#return math.sqrt(a**2 + b**2)

#print(pythagoras(-1, 1))

#creating our own error message using sys.exit()

import sys

def pythagoras(a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)

#Practice

#First: making a function that turns negative numbers into positive numbers

#Function that turns negative numbers into positive numbers

def convert_to_positive(number):
	return abs(number)

#Input from the user; input function is converted to a 'float' to accomodate both integer and decimal numbers
 
number = float(input("Enter a number: "))

#Convert to positive if negative 

positive_number = convert_to_positive(number)

print(f"The positive form of {number} is {positive_number}")

#Second: making a function that calculates area of rectangle

def rectangle_area(length, width):
	area = length * width 
	return area

#Example

length = 20 #length of the rectangle
width = 10 #width of the rectangle
area = rectangle_area(length, width)
print(f"The area of the rectangle is: {area} square units")

#Third: making a function that converts celsius into kelvin

def celsius_to_kelvin (celsius):
	kelvin = celsius + 273.15
	return kelvin

#Example

celsius_temperature = 30 #temperature in degrees celsius
kelvin_temperature = celsius_to_kelvin(celsius_temperature)
print(f"{celsius_temperature}C is equivalent to {kelvin_temperature}K")

#Fourth: making a function that converts kpm to mph

def kph_to_mph(kph):
	mph = kph * 0.621371
	return mph
	
#Example
speed_kph = 180 #speed in kilometers per hour
speed_mph = kph_to_mph(speed_kph)
print(f"{speed_kph} km/h is equivalent to {speed_mph} mph")

#Fifth: function to compute DNA concentration
def calculate_dna_concentration (od260, dna_type='dsDNA'):
	concentration = od260 * 50 #50 ug/mL for double-stranded dna_type
	return concentration

#example
od260_value = 0.5 #example od260 value
dna_concentration = calculate_dna_concentration(od260_value, '50')
print(f"The concentration of the DNA solution is: {dna_concentration} ug/mL")

#if

a = 2
b = 2
if a == b:
	print('a equals b')
	
#Boolean type

c = a == b
print(c)
print(type(c))

#if-elif-else

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

#chaining

a = 3 
b = 4
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print ('you are living in a strange world')
if not False: print (True)

#is_integer function

def is_integer(number):
	return isinstance(number, int)
	
#example

print(is_integer(10))

#DNA complementary function

def complement_dna_letter(nucleotide):
	complement_map = {
	'A' : 'T',
	'T' : 'A',
	'C' : 'G',
	'G' : 'C'
	}
	if nucleotide.upper () not in complement_map:
		raise ValueError(f"Invalid nucleotide: {nucleotide}. Must be 'A', 'T', 'C', or 'G'.")
	return complement_map[nucleotide.upper()]
	
#Example

print(complement_dna_letter('A'))