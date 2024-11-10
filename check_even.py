#Python program to check if the number is even or odd

n = int(input())

def check_even_odd(n): 
  if n%2==0:
    return "Even" 
  else:
    return "Odd"

print(check_even_odd(5)); 
