n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), name, i))

# 나이로 먼저 정렬하고, 나이가 같다면 가입 순서로 정렬
sorted_members = sorted(members, key=lambda x: (x[0], x[2]))

for member in sorted_members:
    print(member[0], member[1])
