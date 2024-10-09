a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    median = a
elif (b > a and b < c) or (b < a and b > c):
    median = b
else:
    median = c

print("The median is", median)
