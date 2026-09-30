def factorial(n):
    result = 1
    for i in range(n):
        result *= i+1

    return result


if __name__ == "__main__":
    print(f"5! = {factorial(5)}")
    print(f"0! = {factorial(0)}")
