#while True:
	#print('hello')

i=0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	print(i)
	i = i + 1
	print('final value of i is', i)
	
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
for i in range(5): print(i)
for i in range (0, 5): print(i)
for i in range (0, 5, 1): print (i)

for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print(nt)

#nested loops
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:		   print(nt1, nt2, '-1')

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:		   print(nt1, nt2, '-1')

#scoring matrix
limit = 4
for i in range(0, limit):
	for j in range (i + 1, limit):
		print (i+1, j+1)

#GC composition algorithm
def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count/ total

print (gc_comp('ACAGCGAAT'))


#triangular number algorithm
def triangular(n):
	tri = 0
	for i in range(n+1):
		tri = tri + 1
	return tri
	
#factorial algorithm
def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range (1, n + 1):
		fac = fac * i
	return fac

#euler algorithm
def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1/ fractorial(n)
	return e

#is_perfect_square algorithm
def is_perfect_square(n):
	root = math.sqrt(n)
	if root %1 == 0: return True
	return False

#is_prime algorithm
def is_prime(n):
	for den in range(2, n//2):
		if n % den == 0: return False
	return True