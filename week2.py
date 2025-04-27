class FactorialCalculator:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        if self.number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result

def main():
    try:
        user_input = int(input("Enter a number to calculate its factorial: "))
        calculator = FactorialCalculator(user_input)
        factorial_result = calculator.calculate()
        print(f"The factorial of {user_input} is: {factorial_result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



class NumberOperations:
    def __init__(self, number):
        self.number = number

    def calculate_factorial(self):
        if self.number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

def main():
    try:
        user_input = int(input("Enter a number: "))
        operations = NumberOperations(user_input)

        factorial = operations.calculate_factorial()
        print(f"Factorial of {user_input} is: {factorial}")

        if operations.is_prime():
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
