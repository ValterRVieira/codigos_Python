def sum_divisors(n):
  sum = 0
  divisors = 1
  while n > divisors:
        if n % divisors == 0:
            sum = divisors+sum
            print ("the divisers of:", str(n) +" are: ", str(divisors))
            divisors +=1
        else:
            divisors +=1
  # Return the sum of all divisors of n, not including n
  return sum

print('the sum of divisers are: '+ str(sum_divisors(0)))
# 0
print('the sum of divisers are: '+ str(sum_divisors(3))) # Should sum of 1
# 1
print('the sum of divisers are: '+ str(sum_divisors(36))) # Should sum of 1+2+3+4+6+9+12+18
# 55
print('the sum of divisers are: '+ str(sum_divisors(102))) # Should be sum of 2+3+6+17+34+51
# 114
