def modulo(a, n):
    # This part finds the quotient of the division. Just returns the integer part.
    # Perform the division where a is the dividend and n is the divisor
    result = a / n
    
    # Extract just the integer part
    quotient = int(result)
        
    # Calculate the modulo (remainder r = a - nq )   
    product = quotient * n
    remainder = a - product
    
    return remainder    
        
# Main program begins

prime_number = int(input( "Enter a prime number ...? " ))       # Ask for a prime number
Pminus1 = prime_number -1                                       # Defines p-1
k=1                                                             # Creates series [1,.. , p-1]
series = []

while k <= Pminus1 :
    series.append(k)
    k += 1
serie = set(series)

print ("The multiplicative serie is\n" + str(serie))
print ("p-1 is\n" + str(Pminus1))


# Begin to test possible generators
generators = []                                            # Creates an empty list for generators
for each_g in series:
    print ("testing g = " + str(each_g))
    possible_serie = []                                    #Creates a serie to compare with the set (1, .., p-1)
    for each_k in series :
        each_g_exp_k = each_g**each_k
        possible_generator = modulo(each_g_exp_k, prime_number)
        possible_serie.append(possible_generator)
    final_serie = set(possible_serie)
    print ("Original Serie " + str(serie))
    print ("Generated Serie " + str(final_serie))
    if serie == final_serie :
        print (str(each_g) + " IS A GENERATOR..!!")
        generators.append(each_g)
print ("The generators of " + str(prime_number) + " are " + str(generators))
        
  