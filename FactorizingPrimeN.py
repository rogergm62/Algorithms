
def prime_factors(n):
    factors = []
    # Start with the smallest prime, 2
    i = 2
    while i <= n:     # We can also use while i <= sqrt(n) for optimization because
                      # No need to check beyond the square root of n
        result = n / i
        quotient = int(result)
        product = quotient * i
        remainder = n - product
            
        if remainder != 0: #If n is not divisible by i, move to the next number
            i += 1
        else:  # If n is divisible by i, divide it and record i as a factor
            factors.append(i)
            n = quotient #This is the new n value
                         
    #if n > 1:                  If we use the condition whiel i <= sqrt(n) we need this condition
    #   factors.append(n)       because if there is any prime factor greater than sqrt(n), it must be n itself
        
    return factors

# Example usage:
number = int(input( "number to factorize ? " ))
print(prime_factors(number))  
