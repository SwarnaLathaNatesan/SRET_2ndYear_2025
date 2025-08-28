import time

def Sum_modulus_hardWay(a,b,c) :
    res = (a + b) % c
    return res


def Sum_modulus(a,b,c) :
    res = ((a % c) +(b%c) ) % c
    return res
    

st = time.time()
print(Sum_modulus(27,15,4))
et = time.time()
print (et-st)

print("Easy Way")
st = time.time()
print(Sum_modulus(2777**277777777,2777**2777,4))
et = time.time()
print (et-st)

print("Hard Way")

st = time.time()
print(Sum_modulus_hardWay(2777**277777777,2777**2777,4))
et = time.time()
print (et-st)

