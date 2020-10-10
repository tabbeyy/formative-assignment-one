import math
prime = 107
is_prime = True

if prime % 2 == 0:
    is_prime = False
if prime % 3 == 0:
    is_prime = False
for i in range(6, math.floor(prime ** 0.5), 6):
    if prime % (i - 1) == 0:
        is_prime = False
    if prime % (i + 1) == 0:
        is_prime = False
if is_prime:
    print(prime, "is prime!")
else:
    print(prime, "is not prime.")