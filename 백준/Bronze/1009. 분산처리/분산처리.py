t = int(input())
results = []

def find_computer(a, b):
    if a == 0:
        return 10
    
    patterns = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6, 4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1, 9, 1],
        0: [10]
    }

    pattern = patterns[a % 10]
    return pattern[(b-1) % len(pattern)]

for _ in range(t):
    a, b = map(int, input().split())
    results.append(find_computer(a, b))

for res in results:
    print(res)
