def factorial(n):
  if n == 0 or n==1:
      return 1
  else:
      return n * factorial(n - 1)

# Test the function
number =int(input("\n Enter the value : "))
result = factorial(number)
print(f"\n The factorial of {number} is {result}")
