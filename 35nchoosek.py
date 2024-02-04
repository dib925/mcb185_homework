#factorial algorithm
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def n_choose_k(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))

demo_values = [(6, 3), (7, 4), (8, 5), (9, 6), (10, 7)]
results = [(n, k, n_choose_k(n, k)) for n, k in demo_values]
print (results)