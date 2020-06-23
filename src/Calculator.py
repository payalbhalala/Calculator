from Csv import CsvReader


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def square(a):
    return a * a

def squareroot(a):
    import math
    return math . sqrt(a)

class Calculator:
    result = 0

    def __init__(self):
        pass


    def add(self, a, b):
        self.result = addition(a, b)
        return self.result


    def subtract(self, a, b):
        self.result = a - b
        return subtraction(a, b)

    def multiply(self, a, b):
        self.result = a * b
        return multiplication(a, b)

    def divide(self, a, b):
        self.result = a / b
        return division(a, b)

    def square(self, a):
      self.result = a * a
      return square(a)

    def squareroot(self, a):
        import math
        math.sqrt(a)