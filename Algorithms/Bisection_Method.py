def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    lower_bound = 0
    upper_bound = max(1, number)

    for _ in range(max_iterations):
        midpoint = (lower_bound + upper_bound) / 2
        square = midpoint * midpoint

        if square == number:
            print(f"The square root of {number} is approximately {midpoint}")
            return midpoint

        if square < number:
            lower_bound = midpoint
        else:
            upper_bound = midpoint

        if upper_bound - lower_bound <= tolerance:
            result = (lower_bound + upper_bound) / 2
            print(f"The square root of {number} is approximately {result}")
            return result

    print(f"Failed to converge within {max_iterations} iterations")
    return None


print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(225, 1e-3, 100))
print(square_root_bisection(225, 1e-5, 100))