num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("First number is: " + str(num1) + " Second number is: " + str(num2))

num1, num2 = num2,num1

print("First number is: " + str(num1) + " Second number is: " + str(num2))