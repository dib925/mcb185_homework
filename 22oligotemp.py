#oligotemp function
def calculate_tm(A, T, G, C):
	oligo_length = A + T + G + C
	if oligo_length <= 13:
		Tm = (A + T) * 2 + (G + C) * 4
	else:
		Tm = 64.9 + 41 * ((G + C - 16.4) / (A + T + G + C))
		
	return Tm
	
#Example

oligos = [{"A": 5, "T": 4, "G": 2, "C": 2}]
for oligo in oligos:
	Tm = calculate_tm(oligo["A"], oligo["T"], oligo["G"], oligo["C"])
	print(f"Oligo (A={oligo['A']}, T={oligo['T']}, G={oligo['G']}, C={oligo['C']}) has Tm = {Tm:.2f} C")

#Example 2
oligos = [{"A": 12, "T": 12, "G": 8, "C": 8}]
for oligo in oligos:
	Tm= calculate_tm(oligo["A"], oligo["T"], oligo["G"], oligo["C"])
	print(f"Oligo (A={oligo['A']}, T={oligo['T']}, G={oligo['G']}, C={oligo['C']}) has Tm = {Tm:.2f} C")

#Example 3
oligos = [{"A": 10, "T": 10, "G": 12, "C": 12}]
for oligo in oligos:
	Tm= calculate_tm(oligo["A"], oligo["T"], oligo["G"], oligo["C"])
	print(f"Oligo (A={oligo['A']}, T={oligo['T']}, G={oligo['G']}, C={oligo['C']}) has Tm = {Tm:.2f} C")