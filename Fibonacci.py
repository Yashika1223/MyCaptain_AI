def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Get user input for the number of Fibonacci numbers to generate
try:
    num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
    fibonacci_sequence = fibonacci_recursive(num_terms)
    print(f"Fibonacci Sequence: {fibonacci_sequence}")
except ValueError:
    print("Please enter a valid positive integer.")
