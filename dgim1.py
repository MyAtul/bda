from dgim import Dgim

stream = list(map(int, input("Enter binary stream: ").split()))
d = Dgim(N=max(1, len(stream)), error_rate=0.1)

for bit in stream:
    d.update(bool(bit))
    print("Bit:", bit, "| Estimate:", d.get_count())

print("Estimated count:", d.get_count())