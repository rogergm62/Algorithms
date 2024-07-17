import time
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
        
print ("Communication intercepted between two host trying to stablish secure")
print ("connection using Diffie-Helman algorithm..!!!")
p = int(input("Prime number p ?"))
g = int(input("Generator g ?"))
A = int(input("Public key ?"))    
print ("A " + '\u2261' + " g**a (mod p)")
input("We are about to strart the program to find the private key a, hit Enter to continue...")
PrivateKey = 1
Aresult = 0
start_time = time.time()
while Aresult != A :
    print("Testing a = " + str(PrivateKey))
    G=g**PrivateKey
    #n= int(input("n? "))
    #a= int(input ("b? "))
    print
    print (f"{G} (mod {p}) \u2261 {modulo(G,p)}")
    PrivateKey +=1 
    Aresult = modulo(G,p)
end_time = time.time()
elapsed_time = end_time - start_time
print("The private key is " + str(PrivateKey-1))
print("time to complete the program :" + str(elapsed_time))
