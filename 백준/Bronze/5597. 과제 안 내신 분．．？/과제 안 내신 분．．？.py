a = set()
b = set(range(1, 31))
c = set()

for i in range(28):
    value = int(input())
    if value>=1 and value<=30:
        a.add(value)

c = b - a
c = sorted(list(c))
print(c[0])
print(c[1])