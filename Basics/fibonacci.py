import time


def fibonacci(n):
    start_time = time.ticks_us()

    if n <= 0:
        fib_sequence = []
    elif n == 1:
        fib_sequence = [0]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    end_time = time.ticks_us()
    duration = end_time - start_time
    print(f"Execution time: {duration} us")
    print(f"First {n} Fibonacci numbers: ", end="")
    print(*fib_sequence, sep=", ")


if __name__ == "__main__":
    fibonacci(10)
