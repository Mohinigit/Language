class A:
    def display(self):
        self.value = "GFG"
        print("I am a parent class -",self.value)
    def show(self):
        print("I am class A")
    def present(self):
        print("Hey Pycharm !! from class A")
class B(A):
    def display(self):
        super().display()
        self.value = "TutorialPoint"
        print("I am a child class -",self.value)
    def sub_show(self):
        print("I am class B")
    def sub_present(self):
        print("Hey Pycharm!! from class B")
class C(B):
    def display(self):
        super().display()
        self.value = "W3Schools"
        print("I am a grandchild class -",self.value)
    def sub_show_1(self):
        print("I am class C")
    def sub_present_1(self):
        print("Hey Pycharm!! from class C")

if __name__ == '__main__':
    a = A()
    a.display()
    a.show()
    a.present()
    b = B()
    b.display()
    b.sub_show()
    b.sub_present()
    c = C()
    c.display()
    c.sub_show_1()
    c.sub_present_1()