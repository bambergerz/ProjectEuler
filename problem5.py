def is_prime(y, z = 2):
	
	"""This function determines if a number y is prime
	
	Output: A boolean. True if y is prime. False otherwise. 
	
	Parameter y: We are trying to determine whether or not this number is prime
	Precondition: y is an int greater than 0. 
	
	Parameter z: the number we are dividing y by to determine whether y is prime. Default value is 2
	Precondition: z is an int greater than 0"""
	
	if y < 2:
		return False
	if z == y:
		return True
	else:
		if y%z == 0:
			a = False
		else:
			a = True
	return a and is_prime(y, z+1)

def factorize(n):
	
	"""This function will take in a number n and produce a list of its prime factors
	
	Output: a list containing the prime factors of n
	
	Parameter n: the number we are trying to factorize
	Precondition: n is an int greater than or equal to 1"""
	
	if is_prime(n):
		return [n]
	x = (n/2) + 1
	while x >= 2:
		if n%x == 0:
			return factorize(x) + factorize(n/x)
		x -= 1
				
def concatonate(m):
	
	"""This function will produce a two dimensional list containing lists of prime factors of numbers from 2 to n.
	
	Output: a two dimensional list containing lists of prime factors of numbers from 2 to n.
	
	Parameter: m is the number until which we will concatenate
	Precondition: m is an int greater than or equal to 1"""
	
	total = []
	for x in range(2, m+1):
		total.append(factorize(x))
	return total
			
def operate(series):
	
	"""This function will return the lowest number which is a multiple of concatenated numbers (see concatonate)
	
	Output: the lowest number which is a multiple of concatenated numbers (see concatonate)
	
	Parameter: series is a two dimensional list containing lists of factors of numbers.
	Precondition: series is a two dimensional list"""
	
	number = 1
	for x in series:
		for y in x:
			number *= y
			for z in series:
				if y in z:
					z.remove(y)
	return number

print operate(concatonate(20))
			
			
		
	
	


