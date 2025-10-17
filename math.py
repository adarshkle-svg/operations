try:
  a= float(input("Enter first number:"))
  b= float(input("Enter seconf number:"))

print(f"Addition:{a+b}")
print(f"substraction:{a-b}")
except ValueError:
print("Please enter valid number.")
