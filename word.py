# Word Count using MapReduce

text = "hello world hello python world hello"

# MAP phase
words = text.split()
mapped = []

for word in words:
    mapped.append((word, 1))

print("Mapped Data:", mapped)

# SHUFFLE phase
grouped = {}

for word, count in mapped:
    if word not in grouped:
        grouped[word] = []
    grouped[word].append(count)

print("Grouped Data:", grouped)

# REDUCE phase
print("Word Count:")

for word, counts in grouped.items():
    print(word, ":", sum(counts))