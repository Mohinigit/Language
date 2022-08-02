try:
    result = 6/0
    print(result)
except ZeroDivisionError:
    print("Number cant be divided by zero!")

'''def throw_err():
    a = 'Choco'
    b = 'Bar'
    print( a % b )
throw_err()'''

num = 10
try:
    n1 = input("Enter first number:")
    n2 = input("enter second number:")
    res = int(n1) // int(n2)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zerodivision Error")
except TypeError:
    print("Type Error")
except:
    print("Unexpected error!")
finally:
    print("always!")
print(res)

a = [1, 2, 3]
try:
    print("Second element = ", a[1])
    print("Fourth element = ", a[3])
except:
    print("An error occurred")


b = [3, 2, 1]
try:
    a == b
except:
    print("They are not equal")
else:
    print("Both Equal")



