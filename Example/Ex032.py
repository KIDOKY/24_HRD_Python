def function1():
    print("Function1")

def function2(func):
    return func()

func = function1
function2(func)