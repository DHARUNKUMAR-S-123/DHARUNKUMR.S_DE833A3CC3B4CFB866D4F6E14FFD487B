# Get the year from the user
year = int(input("\n Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"\n {year} is a leap year")
else:
  print(f"\n {year} is not a leap year")
