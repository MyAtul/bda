import numpy as np

r1, c1 = map(int, input("Rows and columns of A: ").split())
A = np.array([list(map(int, input().split())) for _ in range(r1)])

r2, c2 = map(int, input("Rows and columns of B: ").split())
B = np.array([list(map(int, input().split())) for _ in range(r2)])

if c1 != r2:
    print("Multiplication not possible")
else:
    print("Result Matrix:\n", A @ B)