# student_grades.py

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        try:
            grade = float(grade)
            self.grades.append(grade)
            print(f"✅ Grade {grade} added for {self.name}")
        except ValueError:
            print("❌ Invalid grade. Please enter a number.")

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        grades_str = ', '.join(f"{g:.1f}" for g in self.grades)
        avg = self.average()
        return f"{self.name} | Grades: [{grades_str}] | Average: {avg:.2f}"


class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print("⚠️ Student already exists.")
        else:
            self.students[name] = Student(name)
            print(f"✅ Student '{name}' added.")

    def add_grade(self, name, grade):
        student = self.students.get(name)
        if student:
            student.add_grade(grade)
        else:
            print("❌ Student not found.")

    def show_all(self):
        if not self.students:
            print("📭 No students found.")
        else:
            print("\n📋 Student Grades:")
            for student in self.students.values():
                print(student)
