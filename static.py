class employee:
    section = "HR"
    def __init__(self,name,id):
        self.name = name
        self.id = id

e = employee("Akash",101)
print(employee.section)
print(e.section)

e.section = "Technical"
print(e.section)

employee.section = "Non-Technical"
print(employee.section)

