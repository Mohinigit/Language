file = open("Read.txt","w")
file.write("Hey I am writing to this file\n")

file = open("Read.txt","r")
f_read = file.read()
print(f_read)

file = open("Read.txt","a")
file.write("Hey Pycharm!!\n")
file.write("This is the best IDE")

file = open("Read.txt","r+")
print(file.readline(11))
print(file.readlines())

file = open("Read.txt","r")
file.seek(9)
print(file.read())






