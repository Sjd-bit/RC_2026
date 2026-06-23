class Mylist:
      #
    def __init__(self):
         self.myVariable = "seo"#인스턴스 변수
         self.myVariable2 = "jeong"
         self.myList = list()
    def append(self, ele):#메소드
        self.myList.append(ele)


def main():
    list_a=[1,2,3]
    list_b=[1,2,3]
    list_c=[1,2,3]
    print(list_a+list_b)
    print(list_a)
    list_a.extend(list_b)
    print(list_a)

    list_b.append(7)
    list_b.append(8)
    print(list_b)
    print(list_a+list_b)
    list_b.insert(1, 4.5)
    print(list_b)


    mylist_a = Mylist()
    mylist_a.append("seo jeong dae")
    print(mylist_a.myVariable, mylist_a.myVariable2, mylist_a.myList)

if __name__ == "__main__":
        main()