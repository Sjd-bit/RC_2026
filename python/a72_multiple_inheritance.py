class Person:
    def __init__(self, a):
        self.a = a


class University:
    def __init__(self, b):
        self.b=b 

    def massage

class UnderGraduate(Person, University):
    def __init__(self, c):
        Person.__init__(self, 2)
        University.__init__(self, 3)
        self.c=c   