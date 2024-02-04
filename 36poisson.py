#poisson function algorithm
def factorial(k):
	if k == 0:
		return 1
	else:
		return k * factorial(k-1)

import math

def poisson_probability(n, k):
	return ((n ** k) * (math.e ** -n)) / factorial(k)

demo_values_poisson = [(3, 0), (2.5, 3), (5, 5), (10, 7), (7.5, 10)]
results_poisson = [(n, k, poisson_probability(n, k)) for n, k in demo_values_poisson]
print (results_poisson)