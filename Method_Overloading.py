class A:
    def addition(self,a,b):
        return a + b
    def addition(self,a,b,c):
        return a + b + c

a = A()
print(a.addition(1,2,3))
print(a.addition(1,6.9,5.6))

class B:
    def mul(self,num1,num2):
        return num1 * num2
    def mul(self,num1,num2):
        return num1 ** num2
b = B()
print(b.mul(4,3))

