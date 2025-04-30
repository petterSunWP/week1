# math_tool_static.py

class MathTool:
    @staticmethod
    def factorial(number):
        if number < 0:
            return "❌ Factorial not defined for negative numbers."
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True