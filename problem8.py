def digit_multiple(num, a, b):
	number = 1
	for x in range(a, b):
		number *= get_num(num, x)
	return number

def get_num(number, x):
	return int(str(number)[x])

def greatest_multiple(n, length = 4, b = 3):
	largest_mult = 1
	while b < len(str(n)):
		#print 'largest mult is ' + str(largest_mult)
		#print 'a is ' + str(b-length)
		#print 'b is ' + str(b)
		mult = digit_multiple(n, b-length, b)
		#print 'mult is ' + str(mult)
		if mult > largest_mult:
			#print 'mult > largest_mult --> largest_mult = mult' 
			largest_mult = mult
		if get_num(n,b) == 0 and b+length < len(str(n)):
			#print 'encountered a 0 --> skipping length steps'
			b+=length
		else:
			#print 'adding 1 to b'
			b+=1
	return largest_mult 
	





num = '731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511'
num += '125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749'
num += '303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243'
num += '52584907711670556013604839586446706324415722155397'
num += '536978179778461740649551492908625693219784686224828397224137565705605749026140797296865241453510047482166370484403199890008895243450658541227588666881'
num += '164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408'
num += '071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071760605886116467109405077541002256983155200055935729725'
num += '71636269561882670428252483600823257530420752963450'

print num

print greatest_multiple(int(num), 13, 12)

"""def greatest_multiple(n, a = 0, b = 3, largest_val = 1):
	x = digit_multiple(n, a, b)
	print 'len of n is ' + str(len(str(n)))
	print 'x is ' + str(x)
	print 'a is ' + str(a)
	print 'b is ' + str(b)
	print 'largest_val is ' + str(largest_val)
	if x > largest_val:
		print 'x > largest_val'
		largest_val = x
		print 'largest_val is ' + str(largest_val)
	if b < len(str(n)):
		if get_num(n, b) == 0 and b+13 < len(str(n)):
			greatest_multiple(n, a+13, b+13, largest_val)
		else:
			greatest_multiple(n, a+1, b+1, largest_val)
	return largest_val"""
