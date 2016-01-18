"""
Task: What is the value of the first triangle number to have over five hundred divisors?

Full problem at: https://projecteuler.net/problem=12

To find the n'th triangular number, follow Xn = (n(n+1))/2.

"https://www.mathsisfun.com/algebra/triangular-numbers.html"

According to Stack Overflow: "The number of divisors according to the Divisor function
is the product of the power of each prime factor plus 1.
For example, let's consider the exponential prime representation of 28:

28 = 22 * 30 * 50 * 71 * 110...

The product of each exponent plus one is: (2+1)*(0+1)*(0+1)*(1+1)*(0+1)... = 6,
and sure enough, 28 has 6 divisors.

We will also use the Sieve of Eratosthenes to find primes and the Factorize method
which I developed for problem 5.

To implement the Sieve, make an array of every number leading up to the sqrt(num)+1,
and the slowly eliminate all the numbers that are multiples of n as you move up.

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""


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
		
def exponentiate(n):
	
	"""This function will take in a value n, factorize it, and then return the amount
	of time each prime factor appears in the factorization in the form of a dictionary.
	
	Output: A dictionary which contains factors as key and the amount of times they appear as values of those keys.
	
	Parameter n: the number to exponentiate.
	Precondition: n is an int greater than of equal to 1."""
	
	
	factorization = factorize(n)
	unique = dict()
	for x in factorization:
		if x not in unique:
			unique[x] = 1
		else:
			val = unique[x]
			val+=1
			unique[x] = val
	return unique
			
def num_factors(dictionary):
	
	"""This function will return the number of factors a number will have based on the its exponential form
	(see exponentiate above).
	
	Output: the number of factors of the exponentiated number.
	
	Parameter dictionary: dictionary is a dictionary containing the prime factors of a number and to what power they are raised.
	Precondition: dictionary is a dictionary where they keys are int and the items of those keys are also ints. Ideally the input for this
	function is an output of the exponentiate function."""
	keys = dictionary.keys()
	num = 1 
	for x in keys:
		num*= (dictionary[x]+1)
	return num


def num_triang(n):
	triang = (n*(n+1))/2
	return triang

def five_divisors(n = 1):
	divisors = num_factors(exponentiate(num_triang(n)))
	print 'n is ' + str(n) 
	print 'number of divisors for n: ' + str(divisors)
	if divisors >= 500:
		print 'num_triang(n) is ' + str(num_triang(n))
		return num_triang(n)
	else:
		five_divisors(n+1)
	

print five_divisors(7)




"""Yishai's Comments:

(1) I noticed that you like using recursion instead of a standard loop (for example in 'five_divisors'...
This is usually a bad idea, even though it usually doesn't change how the code works (*usually* because of stack overflows)

(2) I think the factorization will be faster if you start x from 2 and climb to n/2, not the other way around (start from n/2+1) like you did."""





	
"""def sieve(n):
	Creates a list of relevent prime numbers in the range 2...n.
	
	Output: a list of prime numbers in range 2...n
	
	parameter n: the upper limit of the list of primes
	precondition: n is an int greater than 2
	
	primes = []
	for x in range(2, n+1):
		primes.append(x)
	for y in primes:
		mult = 2
		while mult * y <= primes[-1]:
			if (mult*y) in primes:
				primes.remove(mult * y)
			mult+=1
	return primes


#primes = sieve(1000000)
def is_prime(n):
	
	Will check if a particular number 'n' is in the list produced by the sieve f
	unction to determine if n is prime or not.
	
	Output: True if n is a prime, False otherwise.
	
	Parameter n: The number which we are checking for whether or not it is prime.
	Precondition: n is an int >1. 
	
	return n in primes
"""
	
	
