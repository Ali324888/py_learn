from dataclasses import dataclass

name: str = "Adil"
age: int = 30
height: float = 6.5
is_student: bool = True

def multiply(a:int, b:int) -> int:
    return a*b

print(multiply(5, 10))

def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)

print(calculate_total([10, 20, 30, 40]))

def show_marks(marks: dict[str,int]) -> None:
    print(marks)

show_marks({
    "Math": 80,
    "Science": 90,
    "English": 75
})

@dataclass
class Student:
    name: str
    age: int
    marks: list[int]

    def calculate_average(self) -> float:
        return sum(self.marks)/ len(self.marks)

    def is_passing(self) -> bool:
        average = self.calculate_average()
        return average >= 40


student = Student(
    "Adil",
    26,
    [80, 90, 70]
)

print(student)
print(student.calculate_average())