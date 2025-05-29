
def commonDenominator(a, b):

    if b < a:
        a, b = b, a

    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(commonDenominator(12,15))
print(commonDenominator(34,64))
print(commonDenominator(100,50))
print(commonDenominator(13,7))