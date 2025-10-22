def factorial(n):
    val = n
    for i in range(1,n):
        val = val*i
    return val

def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):

    seq = [0,1]
    for i in range(2,n+1):
        new_s = seq[i-1] + seq[i-2]
        seq.append(new_s)
    return seq[n]

if __name__ == "__main__":
    print(f"factorial(2) evaluates to {factorial(2)}")
    print(f"factorial(3) evaluates to {factorial(3)}")
    print(f"factorial(5) evaluates to {factorial(5)}")

    print(f"fib(4) evaluates to {fib(4)}")
    print(f"fib(6) evaluates to {fib(6)}")
    print(f"fib(8) evaluates to {fib(8)}")
    