#Brute Force

def check_prime(n):
  count = 0
  for i in range(1, n):
    if n%i == 0:
      count+=1
  
  if count == 2:
    return "Prime Number"
  else:
    return "Not a Prime NUmber"

n = int(input()); 

print(check_prime(n)); 
