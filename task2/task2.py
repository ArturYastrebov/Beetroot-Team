class Bytes:
    SIZES = {'B': 1, 'KB': 1024, 'MB': 1024 * 1024}

    def __init__(self, size_str):
        size_str = size_str.strip().split()
        self.size = int(size_str[0])
        self.unit = size_str[1]

    def __eq__(self, other):
        return self.to_bytes() == other.to_bytes()

    def __ne__(self, other):
        return self.to_bytes() != other.to_bytes()

    def __lt__(self, other):
        return self.to_bytes() < other.to_bytes()

    def __gt__(self, other):
        return self.to_bytes() > other.to_bytes()

    def to_bytes(self):
        return self.size * self.SIZES[self.unit]

#B > KB > MB
b1 = Bytes('1 KB')
b2 = Bytes('1 MB')
b3 = Bytes('1 B')

print(b1 > b2)   # False
print(b1 == b3)  # False
print(b3 != b2)  # True

