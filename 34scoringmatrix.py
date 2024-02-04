#scoringmatrix algorithm
alphabet = "ACGT"

def print_scoring_matrix(alphabet):
	print(" ", end =' ')
	for letter in alphabet:
		print(letter, end=' ')
	print()
	
	for row in alphabet:
		print(row, end= ' ')
		for col in alphabet:
			if row == col:
				print("+1", end=' ')
			else:
				print("-1", end= ' ')
		print()
	
print_scoring_matrix(alphabet)