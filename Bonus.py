def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 5
num2 = 10

print(GCD(num1, num2))

print(GCD(33, 999))
print(GCD(82428, 6726448))