# check all prime Numbers till N - Naive approach - skeleton

def isPrime(n) :
    #include the prime code function here
    print(n)
    return True
    
counter = 0 
for i in range(1,1001):
    res = isPrime(i)

    if res == True:
        counter = counter + 1
        
print("count of no.s is " ,counter)
        
    
