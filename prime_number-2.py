def prime_check(n):
    if n == 0:
        return False
    if n == 1:
        return False
    count = 0

    for i in range(2, n):
        if (n % i == 0):
            print(str(n) + ' divided by ' + str(i) + ' equals ' + str(n//i))
            count= count + 1
    if (count == 0):
        return True
    else:
        return False

n = 51
result = str(prime_check(n))
print('Result is:' + result)

# comment 2

