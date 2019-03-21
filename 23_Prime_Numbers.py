# Prime Numbers : Only divisible by itself and 1 (2, 3, 5, 7, 11, 13, 17, 19, ...)
# Composite Numbers : Can be factored into smaller integer is called composite number
# Unit 1 -> is Neither prime nor composite
import time
import math

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    for d in range(2, n):
        if n%d == 0:
            return False
        return True

print("="*80)
# ======== Test Function =========
for n in range(1, 21):
    print(n, is_prime_v1(n))

print("="*80)
# ====== Time Function ===========
t0 = time.time()
for n in range(1, 100000):
    is_prime_v1(n)
t1 = time.time()
print("Time required : ", t1 - t0)

print("="*80)
# ======== Making computing factors faster
# For that test all the divisors from from 2 to sqrt(n)
def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# ======== Test Function v2
for n in range(1, 21):
    print(n, is_prime_v2(n))

print("="*80)
# Computing the time required for second function
t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required : ", t1 - t0)

print("*"*80)
def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    
    # if it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor_2 = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor_2, 2): # Third parameter is a step value. This range will start at 3, and cover all odd numbers up to our limit.
        if n % d == 0 :
            return False
        return True

# ====== Test Function 3
for n in range(1, 21):
    print(n, is_prime_v3(n))
print("*"*80)
# Testing Function 3 with Time
t0 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t1 = time.time()
print("Time required : ", t1 - t0)
print("="*80)