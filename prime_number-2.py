def prime_check(n):
    if n == 0:
        return False
    if n == 1:
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False
    else:
        return True

n = 1000
result = str(prime_check(n))
print('Result is:' + result)

