# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = set(map(int, input().split()))
n1 = int(input())
y = set(map(int, input().split()))
x1=x.difference(y)
y1=y.difference(x)
op=sorted(list(x1.union(y1)))
for x in op:
    print(x)
