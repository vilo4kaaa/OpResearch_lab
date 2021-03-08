def Factorial(n):
    if (n < 0):
        return 0
    if (n == 0):
        return 1
    else:
        return n * Factorial(n - 1)


print("Enter ur n:")

n = int(input())

print(n, "! = ", Factorial(n))
