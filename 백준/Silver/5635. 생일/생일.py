N = int(input())
people = []

for _ in range(N):
    parts = input().split()
    name = parts[0]
    day, month, year = map(int, parts[1:])
    people.append((year, month, day, name))
people.sort() 
print(people[-1][3])
print(people[0][3])  
