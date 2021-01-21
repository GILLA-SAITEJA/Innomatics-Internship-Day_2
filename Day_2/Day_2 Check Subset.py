# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(T):
    n=int(input())
    a=set(input().split())
    n1=int(input())
    b=set(input().split())
    print(a.issubset(b))
