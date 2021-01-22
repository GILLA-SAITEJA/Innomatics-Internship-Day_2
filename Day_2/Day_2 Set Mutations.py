# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))
n1 = int(input())

for i in range(n1):

    a, ne = input().split()
    B = set(map(int, input().split()))

    if a == 'intersection_update':
        A.intersection_update(B)

    elif a == 'update':
        A.update(B)

    elif a == 'difference_update':
        A.difference_update(B)

    elif a == 'symmetric_difference_update':
        A.symmetric_difference_update(B)

print(sum(A))
