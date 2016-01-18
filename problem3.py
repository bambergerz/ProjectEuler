def is_prime(y, z = 2):
	if y < 2:
		return False
	if z == y:
		return True
	else:
		if y%z == 0:
			#print 'initiating if...'
			a = False
			#print 'y is ' + str(y)
			#print 'z is ' + str(z)
			#print 'a is ' + str(a)
		else:
			#print 'initiating else...'
			a = True
			#print 'y is ' + str(y)
			#print 'z is ' + str(z)
			#print 'a is ' + str(a)
	return a and is_prime(y, z+1)

def is_prime2(num):
	"""Alternative developed by Yishai Gronich"""
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True

def highest_prime_2(num):
	"""Developed by Yishai Gronich: Divide by any factor of num, until num is prime """
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return highest_prime_2(num / i)
	return num
		
			
