from student import Student

class Storage:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        self.students[student_id] = Student(student_id, name)

    def get_student(self, student_id):
        return self.students.get(student_id)

    def add_marks(self, student_id, score):
        student = self.get_student(student_id)
        if student:
            student.add_marks(score)
        else:
            print("Student not found!")

    def show_all(self):
        for sid, student in self.students.items():
            print(f"\nID: {sid}")
            print(f"Name: {student.name}")
            print(f"Marks: {student.marks}")
            print(f"Average: {student.average():.2f}")