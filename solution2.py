# Write code for algorithm 2 below
def natural_numbers(x, i):
    if x > i:
        return
    else:
        print(x)
        natural_numbers(x + 1, i)
n=10
print(natural_numbers(1, n))