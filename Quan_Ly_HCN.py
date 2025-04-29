class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display_info(self):
        print(f"Chiều rộng hình chữ nhật: {self.width}")
        print(f"Chiều cao hình chữ nhật:  {self.height}")
        print(f"Diện tích hình chữ nhật:  {self.area()}")
        print(f"Chu vi hình chữ nhật:     {self.perimeter()}")

w = float(input("Nhập chiều rộng hcn: "))
h = float(input("Nhập chiều cao hcn:  "))

rect = Rectangle(w, h)
rect.display_info()
