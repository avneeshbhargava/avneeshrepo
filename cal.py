class calu():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self):  # it can be any varibale
        return self.a + self.b  # this should be same as init method variable

    def subtract_fun(self):
        return self.a - self.b

    def divide_function(self):
        return self.a / self.b

    def multiply_function(self):
        return self.a * self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = calu(a, b)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.Add())
    elif choice == 2:
        print(obj.subtract_fun())
    elif choice == 3:
        print(obj.multiply_function())
    elif choice == 4:
        print(obj.divide_function())
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
