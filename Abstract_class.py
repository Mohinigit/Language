from abc import ABC,abstractmethod

class Company(ABC):
    def company_info(self):
        print("Welcome to Biocon")
    @abstractmethod
    def project(self):
        "Abstract Method"
        pass
class Biocon(Company):
    def project(self):
        "Implementation of abstract method"
        print("In Biocon, Downstream processing dept is interesting!")
class Ajanta(Biocon):
    def project(self):
        "Other implementation of abstract method"
        print("In Ajanta, Quality control is best dept for entry level employees")

a = Ajanta()
a.project()
a.company_info()
