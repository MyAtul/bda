from bloom_filter2 import BloomFilter

bloom = BloomFilter(max_elements=100,error_rate=0.01)
numbers = [10,20,30,40,50,60,70]

for n in numbers:
    bloom.add(str(n))

search = input("Enter number:")

print("Possibly present" if search in bloom else "Definitly not present")