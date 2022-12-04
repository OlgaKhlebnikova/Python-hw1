def sum(x):
    return x+10

def mult(x):
    return x**2

print(sum(2))
print (mult(2))

print (sum(mult(2)))

sum1 = lambda x: x+10
mult1 = lambda x: x**2

sum(mult1(2))

print(sum1(mult1(2)))