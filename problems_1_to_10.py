from math import sqrt, floor
# Problem 1
# Find the sum of all the multiples of 3 or 5 below n

def sum_multiples(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s

print(sum_multiples(1000))

# Problem 2
# Find the sum of the even-valued Fibonacci terms below n

def sum_even_fib(n):
    s = 2
    f = [1, 2] # initialisation

    while f[-1] < n:
        f_n = f[-1]+f[-2]
        f.append(f_n)
    
        if f_n % 2 == 0:
            # Adding only the even Fibonacci numbers
            s += f_n
    return s

print(sum_even_fib(4000000))

# Problem 3
# Find the largest prime factor of n
def largest_prime_factor(n):
    i = 2
    while i < sqrt(n):
        print(i)
        if n % i == 0:
            n /= i
            print(n, i)
        else:
            i += 1
    return int(n)

print(largest_prime_factor(600851475143))

# Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindrome_list = [i*j for i in range(100,1000) for j in range(i,1000) if is_palindrome(i*j)]
print(max(palindrome_list))


# Problem 5
# Find the smallest positive number that is divisible by all of the numbers from 1 to n

def smallest_multiple(n):
    # We can start from n, and increment by n, since it must be divisible by n.
    # We can stop at n!, since the number is definitely smaller than that.
    i = n
    while True:
        if all(i % j == 0 for j in range(1,n+1)):
            return i
        else:
            i += n

print(smallest_multiple(20))

# Problem 6
# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum
# We can use the formulas
def sum_square_diff(n):
    return int((n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6)
print(sum_square_diff(100))

# Problem 7
# Find the nth prime number

def nth_prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if all(i % j != 0 for j in primes):
            primes.append(i)
        i += 2
    return primes[-1]

print(nth_prime(10001))

# Problem 8
# Find the n adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product? 

N = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

def greatest_product(n, N):
    max_prod = 0
    
    for i in range(len(N)-n):
        prod = 1

        for j in range(n):
            prod *= int(N[i+j])

        if prod > max_prod:
            max_prod = prod
    return max_prod

print(greatest_product(13, N))

# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet_summing_to_(n):
    for a in range(1,n):
        for b in range(a,n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                print(a,b,c)
                return a*b*c

print(pythagorean_triplet_summing_to_(1000))

# Problem 10
# Find the sum of all the primes below n

def is_prime(x):
    # Returns True if x is prime, False otherwise
    bool = True   
    for i in range(2,floor(sqrt(x)+1)):
        if (int(x) % i)==0:
            bool=False
            break
    return bool

sum=2
for i in range(3,2000000):
    if is_prime(i):
        sum = sum + i

print(sum)