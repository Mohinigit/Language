'''arr = []
limit = int(input("Enter the max limit:"))
for val in range(limit):
    n = int(input("Enter a number:"))
    arr.append(n)

def add(arr):
    sum_arr = sum(arr)
    print(sum_arr)
add(arr)

def avg(arr):
    avg_arr = sum(arr)/len(arr)
    print(avg_arr)
avg(arr)'''

array = [3,6,8,8,5,2,2,8]

index = array.index(6)
print("Index of 6 is ",index)

def check(array):
    if 6 in array:
        print(True)

check(array)

def remove(array):
    for val in range(0,len(array)):
        if val == 2:
            array.remove(val)
    print(array)
remove(array)

def copy(array):
    new_arr = array.copy()
    print(new_arr)
    print(id(new_arr),id(array))
copy(array)

def insert(array):
    array.insert(2,7)
    print(array)

insert(array)

def sort(array):
    array.sort()
    print("Minimum = ",array[0])
    print("Maximum = ",array[-1])

sort(array)

def rev(array):
    res = array[::-1]
    print(res)

rev(array)

def dup(array):
    for val in array:
        new = []
        if array.count(val) > 1:
            new.append(val)
    print(new)

dup(array)

arr1 = [4,6,9,2]
arr2 = [5,1,8,2]
print(set(arr1).intersection(set(arr2)))

def remove_dup(array):
    for val in array:
        if array.count(val) > 1:
            array.remove(val)
    print(array)

remove_dup(array)

def sec_large(array):
    array.sort()
    array.pop(-1)
    print("Second largest Number:",array[-1])
sec_large(array)

def count(array):
    even_count = 0
    odd_count = 0
    for val in array:
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Count of even numbers:",even_count)
    print("Count of odd numbers:", odd_count)

count(array)

def diff(array):
    array.sort()
    result = array[-1] - array[0]
    print("Difference between the largest and smallest number:",result)

diff(array)



