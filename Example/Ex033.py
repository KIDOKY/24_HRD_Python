def print_n_times(n, *args):
    for i in range(n):
        for arg in args:
            print(arg)
        print()

print_n_times(3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def function(param1 = 0, param2 = 0):
    return param1 + param2

function()