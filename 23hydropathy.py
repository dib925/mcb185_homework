#hydropathy equation
def get_kyte_doolittle_value(amino_acid):
	kd_values = {
	'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5,
	'M': 1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
	}
	return kd_values.get(amino_acid.upper(), None)

#Example
amino_acids = ['A', 'W', 'G', 'Z']
for aa in amino_acids:
	kd_value = get_kyte_doolittle_value(aa)
	if kd_value is not None:
		print(f"The Kyte-Doolittle value for {aa} is {kd_value}")
	else:
		print(f"{aa} is not a valid standard amino acid letter")

#Example 2
amino_acids = ['F', 'W', 'Y', 'W']
for aa in amino_acids:
	kd_value = get_kyte_doolittle_value(aa)
	if kd_value is not None:
		print(f"The Kyte-Doolittle value for {aa} is {kd_value}")
	else:
		print(f"{aa} is not a valid standard amino acid letter")

#Example 3
amino_acids = ['Y', 'Y', 'H', 'H']
for aa in amino_acids:
	kd_value = get_kyte_doolittle_value(aa)
	if kd_value is not None:
		print(f"The Kyte-Doolittle value for {aa} is {kd_value}")
	else:
		print(f"{aa} is not a valid standard amino acid letter")

#Example 4
amino_acids = ['Z', 'Z', 'Z', 'Z']
for aa in amino_acids:
	kd_value = get_kyte_doolittle_value(aa)
	if kd_value is not None:
		print(f"The Kyte-Doolittle value for {aa} is {kd_value}")
	else:
		print(f"{aa} is not a valid standard amino acid letter")
