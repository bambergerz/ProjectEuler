from datetime import timedelta


def is_prime(num):
	"""Ensures that num is not divisible by any number between 2 and its square root + 1
	
	Output: Boolean. True if prime. False otherwise.
	
	Parameter num: the number we are checking to see if prime.
	Precondition: n is an int greater than 0."""
	
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True

def sum_below(n):
	
	total = 5
	num = 3
	while num+1 < n:
		num+=2
		#print 'num is ' + str(num)
		if is_prime(num):
			total+=num
			#print 'total is ' + str(total)
	return total 
