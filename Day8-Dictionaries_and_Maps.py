import sys

n = int(input())
phonebook ={}
for _ in range(n):
    name,number = input().split()
    phonebook[name]=number

for query in sys.stdin:
    val = query.strip()
    if val in phonebook:
        print(f"{val}={phonebook[val]}")
    else:
        print("Not found")  