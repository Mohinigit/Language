def arith_op(a,b):
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a % b =", a % b)
    print("a / b =", a / b)
    print("a * b =", a * b)

arith_op(26,13)

def operations(num1,num2):
    print("\nBefore incrementing and decrementing:",num1,num2)
    num1+=2
    num2-=3
    print("After incrementing and decrementing:",num1,num2)

operations(34,87)

a = int(input("\nEnter first number:"))
b = int(input("Enter second number:"))
if a == b:
    print("The two numbers are equal")
else:
    print("The two numbers are not equal")

a = float(input("\nEnter first number:"))
b = float(input("Enter second number:"))
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


a = int(input("\nEnter a number:"))
b = int(input("Enter a number again!:"))
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

if a < b:
    print(f"{a} is smaller")
else:
    print(f"{b} is smaller")




