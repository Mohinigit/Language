class Parent:
    name = "Michael"
    _name = "Genelia"
    __name = "George"
    def pub_display(self):
        print("Public Data Members:",self.name)
    def _pro_display(self):
        print("Protected Data Members:",self._name)
    def __pri_display(self):
        print("Private Data Members:",self.__name)
    def Public_display(self):
        self.__pri_display()
class Child(Parent):
    def Protected_display(self):
        self._pro_display()


if __name__ == '__main__':
    obj = Child()
    obj.Protected_display()
    obj.Public_display()
    obj.pub_display()



