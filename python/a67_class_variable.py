from pathlib import Path


class Student:
    count = int()


    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1 
    def get_sum(self):
        return self.korean + self. math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"

    def __eq__(self, value):
        if isinstance(value, Student):
            return self.get_sum() == value.get_sum()
        else:
            raise ValueError

    def __ne__(self, value):
        if isinstance(value, Student):
            return self.get_sum() != value.get_sum()
        else:
            raise ValueError

    def __gt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() > value.get_sum()
        else:
            raise ValueError

    def __ge__(self, value):
        if isinstance(value, Student):
            return self.get_sum() >= value.get_sum()
        else:
            raise ValueError

    def __lt__(self, value):
        if isinstance(value, Student):
            return self.get_sum() < value.get_sum()
        else:
            raise ValueError

    def __le__(self, value):
        if isinstance(value, Student):
            return self.get_sum() <= value.get_sum()
        else:
            raise ValueError


def main():
    student_path = Path(__file__).parent.parent / "data/student_info.data"
    students = []
    with open(student_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, korean, math, english, science = line.split()

            student = Student(name, int(korean), int(math), int(english), int(science))
            students.append(student)
    print(f"현재 총 학생 수는 {Student.count}")

    print("이름\t총점\t평균")
    for student in students:
        print(student)



if __name__ == "__main__":
    main()