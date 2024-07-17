# This program will find the Modulo. Python has a function for this algorith %
# This program reproduces the same result.

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
        
    
print ("a " + '\u2261' + " b (mod n)")
n= int(input("n? "))
a= int(input ("b? "))
print
print (f"{a} (mod {n}) \u2261 {modulo(a,n)}")
