#pythagoreas triple algorithm
def find_pythagorean_triples(max_side):
	triples = []
	for a in range(1, max_side):
		for b in range(a, max_side):
			c_square = a**2 + b**2
			c = c_square**0.5
			if c.is_integer():
				triples.append((a, b, int(c)))
	return triples

pythagorean_triples = find_pythagorean_triples(100)
print(pythagorean_triples)