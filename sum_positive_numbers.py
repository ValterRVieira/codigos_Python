def sum_positive_numbers(n):
    if n==0:
        return 0
    return n + sum_positive_numbers(n-1)

print (sum_positive_numbers(10))
print (sum_positive_numbers(20))