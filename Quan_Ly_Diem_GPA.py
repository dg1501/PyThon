class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def display_info(self):
        print(f"{self.name} | {self.student_id} | GPA: {self.gpa}")

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

students = []

n = int(input("Nhập số lượng sinh viên: "))
for _ in range(n):
    name = input("Tên: ")
    student_id = input("Mã SV: ")
    gpa = float(input("GPA: "))
    students.append(Student(name, student_id, gpa))

print("\nDanh sách sinh viên ban đầu:")
for s in students:
    s.display_info()

print("\nCập nhật GPA mới cho từng sinh viên ")
for s in students:
    new_gpa = float(input(f"Nhập GPA mới cho {s.name} (Mã SV: {s.student_id}): "))
    s.update_gpa(new_gpa)

print("\nDanh sách sinh viên sau cập nhật:")
for s in students:
    s.display_info()
