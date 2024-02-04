#Fizzbuzz solution algorithm
for num in range(1, 100):
	string = ""
	if num % 3 == 0:
		string = string + "Fizz"
	if num % 5 == 0 :
		string = string + "Buzz"
	if num % 3 == 0 and num % 5 == 0:
		string = string + "FizzBuzz"
	print(string)