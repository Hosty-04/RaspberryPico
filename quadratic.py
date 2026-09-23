from math import sqrt


def solve_quadratic(a, b, c):
    results = []

    D = b**2-4*a*c

    if D > 0:
        x1 = (-b+sqrt(D))/(2*a)
        x2 = (-b-sqrt(D))/(2*a)
        results.extend([x1, x2])

    elif D == 0:
        x = -b/(2*a)
        results.append(x)

    else:
        results.append("No real solutions")

    return results


if __name__ == "__main__":
    print("Solution(s): ", end="")
    print(*solve_quadratic(1, -3, 2), sep=", ")

    print("Solution(s): ", end="")
    print(*solve_quadratic(1, 2, 1), sep=", ")

    print("Solution(s): ", end="")
    print(*solve_quadratic(1, 1, 1), sep=", ")
