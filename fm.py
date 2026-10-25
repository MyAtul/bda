def hash1(x):
    return (5*x + 3) % 16

def trailing_zero(n):
    if n == 0:
        return 4
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count

data = list(map(int, input("Enter stream: ").split()))

hash_values = [hash1(i) for i in data]
binary = [bin(i)[2:] for i in hash_values]
zero = [trailing_zero(i) for i in hash_values]

print("Hash values:", hash_values)
print("Binary values:", binary)
print("Trailing zeros:", zero)
print("Actual Distinct Elements:", len(set(data)))
print("Estimated Unique Elements:", 2 ** max(zero))