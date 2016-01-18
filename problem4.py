
def is_pal(n):
	"""determines if n is a palindrome. Returns True if it is and False otherwise.
	Parameter n: an integer """
	first_digit = n%10
	last_digit = int(str(n)[0])
	if len(str(n)) == 1:
		return True
	elif len(str(n)) == 2:
		if first_digit == last_digit:
			return True
		else:
			return False
	#elif len(str(n)) == 3 and first_digit == last_digit:
		#return True 
	else:
		if first_digit != last_digit:
			return False
		else:
			new_n = str(n)
			new_n = int(new_n[1:len(new_n)-1])
			return True and is_pal(new_n)
		
def largest_prod_pal(a = 999, b=999):
	while a > 99:
		while b > 99:
			if (is_pal(a*b)):
				return a*b
			b-= 1
		a-=1
		
	
	
