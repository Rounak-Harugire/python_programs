def simple_interest( p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    
    simple_interest = (p * t * r)/100
    
    print('The Simple Interest is', simple_interest)
    return simple_interest
    
simple_interest(3, 4, 5)