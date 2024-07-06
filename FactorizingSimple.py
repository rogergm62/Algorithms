def prime_factors(n):
    factors = [] # Creates an empty list to store factors
    # Start with the smallest prime, 2
    i = 2
    while i <= n:    
        result = n / i
        quotient = int(result)
        product = quotient * i
        remainder = n - product
            
        if remainder != 0: #If n is not divisible by i, move to the next number
            i += 1
        else:  # If n is divisible by i, divide it and record i as a factor
            factors.append(i)
            n = quotient #This is the new n value
    
    return factors

number = int(input( "number to factorize ? " ))
print(prime_factors(number))  
