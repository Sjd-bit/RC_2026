import math

class Circle:
    def__init__(self, radius):
        self.__radius = radius
    
def main():
    c=Circle(5)
    print(c.__dict__)
    print(c._Circle__radius)




if __name__ == "__main__":
        main()
