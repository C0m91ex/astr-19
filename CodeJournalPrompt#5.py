# Coding Journal Prompt #5

import numpy as np 

# This function will generate the sin values for the table
def generate_sin_table(start, end, number_points):
	x = np.linspace(start, end, number_points)
	sin_x = np.sin(x)
	table = list(zip(x, sin_x))
	return table 

# This function will print out the table
def print_sin_table(table):
	print("x\t| sin(x)")
	print("-" * 15)
	for x, sin_x in table:
		print(f"{x:.4f}\t| {sin_x:.4f}")

# This is the main calling function
def main():
	start = 0
	end = 2 * np.pi 
	number_points = 1000

	sin_table = generate_sin_table(start, end, number_points)
	print_sin_table(sin_table)

if __name__ == "__main__":
	main()
