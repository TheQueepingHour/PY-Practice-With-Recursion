# Write code for algorithm 3 below
def fibonacci(x):
    if x <= 0:
        print("invalid")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    
print(fibonacci(4))