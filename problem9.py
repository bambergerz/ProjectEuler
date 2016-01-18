"""
Accoding to Jonathan Gal:

A=m^2-n^2
B=2mn
C=m^2+n^2
For every m>n>0 there is a triplet
Choose m if n is a natural number and smaller than m"""

def get_special_triplet():
	"""credit to Yishai Gronich for the idea of imbedded for loop with conditional pythag and triangle-side-rule combination
	
	This function produces the multiple of a, b, and c where the three are a pythagorian triplet and a<b<c"""
	
	for c in range(1001):
		for b in range(c):
			a = 1000 - c - b
			if 0 < a < b and  a**2 + b**2 == c**2:
				print 'a is ' + str(a)
				print 'b is ' + str(b)
				print 'c is ' + str(c)
				return a*b*c
			
	
