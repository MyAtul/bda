size = 10
bit_array = [0] * size

def hash1(x):
    return (2*x*x + 3*x + 1) % size

def hash2(x):
    return (x*x*x + 2*x + 4) % size

def add(x):
    bit_array[hash1(x)] = 1
    bit_array[hash2(x)] = 1

def check(x):
    if bit_array[hash1(x)] and bit_array[hash2(x)]:
        print(x, "may be present")
    else:
        print(x, "is definitely not present")

numbers = [10, 20, 30,40,50,1,3]
for x in numbers:
    add(x)

print("Bit array:", bit_array)

search = list(map(int, input("Enter numbers to search: ").split()))
for x in search:
    check(x)