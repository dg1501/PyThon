class Employee:
    def __init__(self, name, salary):
        self.name = name           # Public attribute
        self._salary = salary      # Private attribute

    def display_info(self):
        print(f"Tên: {self.name} | Lương: {self._salary} | Thuế thu nhập: {self.get_tax()}")

    def _calculate_tax(self):
        return self._salary * 0.1   

    def get_tax(self):
        return self._calculate_tax()

n = int(input("Nhập số lượng nhân viên: "))
employees = []

for i in range(n):
    print(f"\nNhân viên {i+1}:")
    name = input("Nhập tên nhân viên: ")
    salary = float(input("Nhập lương nhân viên: "))
    emp = Employee(name, salary)
    employees.append(emp)

print("\nDANH SÁCH NHÂN VIÊN")
for emp in employees:
    emp.display_info()
