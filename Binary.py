
n = int(input("Enter N "))
A = [0] * n

""" Fn to generate all binary numbers for a given digit"""
def binary(n):
    if n < 1:
        print(A)

    else:
        A[n-1] = 0
        binary(n - 1)
        A[n-1] = 1
        binary(n - 1)


binary(n)