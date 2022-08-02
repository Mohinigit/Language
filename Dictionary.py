Dict = {}
Dict = dict({1:"Rucha", 2:"Nikhil", 3:"Kalpesh"})
print(Dict)

Dict[4] = "Viral"
print(Dict)

Dict.update({2:"Karan"})
print(Dict)

print(Dict[3])

Dict.update({3:{1:"Mahesh"}})
print(Dict)

print(Dict[3][1])

print(Dict.keys())

del(Dict[1])
print(Dict)
