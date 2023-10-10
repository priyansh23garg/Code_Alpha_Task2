def fibonacci_generator(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the size of series: "))
fibonacci_numbers = fibonacci_generator(n)
print("Fibonacci Sequence:")
print(fibonacci_numbers)

