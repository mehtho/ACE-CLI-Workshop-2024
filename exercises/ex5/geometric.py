def geometric(n):
    # Return a list of the first n numbers in a geometric sequence
    # i.e [1, 2, 4, 8, ..., 2^(n-1)]
    pass


def check(ans, n):
    if ans == [(2**(i - 1)) for i in range(1, n + 1)]:
        print("Success")
    else:
        print("Try Again")

check(geometric(8), 8)
