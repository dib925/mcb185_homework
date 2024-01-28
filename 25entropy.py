#entropy function
import math

def calculate_shannon_entropy(a, c, g, t):
	total = a + c + g + t
	entropy = 0
	nucleotides = [a, c, g, t]
	for count in nucleotides:
		if count > 0:
			probability = count / total
			entropy -= probability * math.log2(probability)
	
	return entropy
	
#Example 1
test_cases = [{'a': 25, 'c': 25, 'g': 25, 't': 25}]
for case in test_cases:
	entropy = calculate_shannon_entropy(case['a'], case['c'], case['g'], case['t'])
	print(f"Nucleotide counts A:{case['a']}, C:{case['c']}, G:{case['g']}, T:{case['t']} have Shannon entropy: {entropy:.4f}")

#Example 2
test_cases = [{'a': 30, 'c': 20, 'g': 20, 't': 30}]
for case in test_cases:
	entropy = calculate_shannon_entropy(case['a'], case['c'], case['g'], case['t'])
	print(f"Nucleotide counts A:{case['a']}, C:{case['c']}, G:{case['g']}, T:{case['t']} have Shannon entropy: {entropy:.4f}")

#Example 3
test_cases = [{'a': 50, 'c': 0, 'g': 0, 't': 50}]
for case in test_cases:
	entropy = calculate_shannon_entropy(case['a'], case['c'], case['g'], case['t'])
	print(f"Nucleotide counts A:{case['a']}, C:{case['c']}, G:{case['g']}, T:{case['t']} have Shannon entropy: {entropy:.4f}")
			