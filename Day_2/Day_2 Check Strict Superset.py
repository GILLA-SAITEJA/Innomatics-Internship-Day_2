# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
for _ in range(int(input())):
    if not a.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)
