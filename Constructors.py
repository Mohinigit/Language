class A:
    def __init__(self):
        print("It is default constructor")

    def __init__(self, name):
        self.name = name

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        return self.name, self.id


a = A("Akash", 102)
print(a.display())


class A:
    name = None
    _id  = None
    __dept = None
    def __init__(self,name,_id,__dept):
        self.name = name
        self._id = _id
        self.__dept = __dept
    def show_name(self):
        print("Name:",self.name)
    def _show_id(self):
        print("Id:",self._id)
    def __show_dept(self):
        print("Department:",self.__dept)
    def access_private_method(self):
        self.__show_dept()
class B(A):
    def __init__(self,name,_id,__dept):
        super().__init__(name,_id,__dept)
    def access_protected_method(self):
        self._show_id()

b = B("Rakshita",234,"HR")
b.show_name()
b.access_private_method()
b.access_protected_method()


