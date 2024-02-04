#estimation of pi using Nilakantha series
def estimate_pi_nilakantha(terms):
	pi_estimate = 3
	sign = 1

	for i in range(2, 2 * terms, 2):
		pi_estimate += sign * (4 / (i * (i + 1) * (i + 2)))
		sign *= -1
	
	return pi_estimate

estimate_pi = estimate_pi_nilakantha(1000)
print(estimate_pi)