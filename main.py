from calculator import add, subtract, multiply, divide

def main():
    result_add = add(10, 5)
    result_subtract = subtract(10, 5)
    result_multiply = multiply(10, 5)
    result_divide = divide(10, 5)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")
    print(f"Division: {result_divide}")

    return 0

if __name__ == "__main__":
    main()

