# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(input().split())
n1=int(input())
b=set(input().split())
print(len(a.symmetric_difference(b)))
