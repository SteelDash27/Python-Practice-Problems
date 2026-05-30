
def countdown(n: int):
    if n == 1:
        print(n)
        return
    else:
        print(n)
        n = n - 1
        countdown(n)   # not n-1 again

number = 10
countdown(number)
