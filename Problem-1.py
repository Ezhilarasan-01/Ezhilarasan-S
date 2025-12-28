class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        operation = operation.lower()
        
        if operation == "+":
            return self.a + self.b
        elif operation == "-":
            return self.a - self.b
        elif operation == "*":
            return self.a * self.b
        elif operation == "/":
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid operation"


val_1 = float(input("Enter a: "))
val_2 = float(input("Enter b: "))
op_type = input("Enter type of operation (addition=+, subtraction=-, multiplication=*, division=/): ")

my_calc = Calculator(val_1, val_2)
result = my_calc.calculate(op_type)

print(f"Result: {result}")