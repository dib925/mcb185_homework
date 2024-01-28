#Quadratic formula
import cmath #cmath module includes support for complex numbers

def solve_quadratic (a, b, c):
	discriminant = cmath.sqrt(b**2 - 4*a*c)
	root1 = (-b + discriminant) / (2*a)
	root2 = (-b - discriminant) / (2*a)
	
	return root1, root2

#Example
a, b, c = 2, -6, 4 
root1, root2 = solve_quadratic(a, b, c)
print(f"The roots are: {root1} and {root2}")