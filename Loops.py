a_string = 'Bright IT Career'
for i in range(10):
    print(a_string)

print('\n')

i = 1
while i <= 20:
    print(i)
    i+=1

print('\n')

a = 6
b = 9
print(a == b)
print(a != b)

print('\n')

n = int(input("Enter maximum limit:"))
print("Even numbers:")
for i in range(1,n):
    if i % 2 == 0:
        print(i, end = " ")
print("\n Odd numbers:")
for i in range(1,n):
    if i % 2 != 0:
        print(i, end = " ")

print('\n')

a = 98
b = 67
c = 43
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c
print("Largest number is",largest)

print('\n')

a = 10
b = 20
while a < b:
    if a % 2 == 0:
        print(a)
    a+=1

print('\n')

i = 1
while True:
    print (i)
    i+=1
    if i > 10:
        break

print('\n')

n = int (input("Enter a number:"))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")

print('\n')

n = int (input("Enter a number:"))
for i in range(2,n):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")

print('\n')

str = "madam"
new_str = str[::-1]
if str == new_str:
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")
