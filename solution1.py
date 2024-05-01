# Write code for algorithm 1 below
def iterate(num):
    if num == 0:
        return 0
    else:
        print(num)
        iterate(num-1)

n = 4
iterate(n)