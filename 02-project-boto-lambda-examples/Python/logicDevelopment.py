num1 = int(input("Enter the first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    print(num1, "is greater than: ", num2)
elif(num1==num2):
    print(num1, "is equal to: ", num2)
else:
    print(num1, "is smaller than: ", num2)