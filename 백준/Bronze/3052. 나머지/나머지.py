mod = [0] * 10
for i in range(10) :
    mod[i] += int(input()) % 42
print(len(set(mod)))

