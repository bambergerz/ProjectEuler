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

def is_prime2(num):
	"""Ensures that num is not divisible by any number between 2 and its square root + 1
	
	Output: Boolean. True if prime. False otherwise.
	
	Parameter num: the number we are checking to see if prime.
	Precondition: n is an int greater than 0."""
	
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True


def count_primes(n):
	"""This function determines the n'th number prime.
	
	Output: The n'th prime
	
	Parameter n: the number prime we are looking for.
	Precondition: n is an int greater than 2"""
	
	num_primes = 2
	x = 3
	
	while num_primes < n:
		x+=2
		if is_prime2(x):
			num_primes+=1
			#print 'num is ' + str(num_primes)
		
		#print 'x is ' + str(x)
		
	return x
	
	
