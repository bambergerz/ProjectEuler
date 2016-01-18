def check_num(num = 1000):
    total = 0  
    list1 = range(num)
    for x in list1:
        #print list1
        if x % 3 == 0 or x%5 ==0:
            #print str(x) + ' works'
            total = total + x
    return total 

