
# Input matrix A
r1 = int(input("Rows of A: "))
c1 = int(input("Columns of A: "))
A = [list(map(int, input().split())) for _ in range(r1)]

# Input matrix B
r2 = int(input("Rows of B: "))
c2 = int(input("Columns of B: "))
B = [list(map(int, input().split())) for _ in range(r2)]

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    # MAP phase
    mapped = []
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                mapped.append(((i, j), A[i][k] * B[k][j]))

    # SHUFFLE phase
    grouped = {}
    for key, value in mapped:
        grouped.setdefault(key, []).append(value)

    # REDUCE phase
    C = [[sum(grouped[(i, j)]) for j in range(c2)]
         for i in range(r1)]

    # Display result
    print("Resultant Matrix:")
    for row in C:
        print(*row)
