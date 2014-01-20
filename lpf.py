def lpf(num):
  i = 3
  result = set([1])
  if not num % 2:
    result.add(2)
  while i < ((num/2)+1):
    if not num % i and is_prime(i):
      num = num/i
      result.add(i)
      i = 3
    else :
      i += 2
  result.add(num)
  return max(result)

def is_prime(num):
  if num == 2:
    return True
  if not num % 2:
    return False
  i = 3
  while i < (num/2 + 1):
    if not num % i:
      return False
    i += 2
  return True

import time
s = time.time()
print lpf(600851475143)
print time.time() - s
