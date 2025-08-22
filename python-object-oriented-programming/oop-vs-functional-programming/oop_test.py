# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Object Oriented Programming code
#  Author       : Team Tinitiate
# ==============================================================================



class OOP:
    # Class Variables
    n1 = None
    n2 = None
            
    # Class Methods(Functions)
    def print_class_vars(self):
        print("Class OOPs vars:")
        print("n1=",self.n1)
        print("n2=",self.n2)

    def add1(self):
        return self.n1 + self.n2

    def mul1(self):
        return self.n1 * self.n2
