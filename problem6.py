
def sum_of_squares(n = 100):
	total = 0 
	for x in range(1,n+1):
		total+= x**2
	return total

def sqaure_of_sums(n = 100):
	sum_nums = 0
	for x in range (1,n+1):
		sum_nums+=x
	return sum_nums**2

print sqaure_of_sums(100) - sum_of_squares(100)
	
