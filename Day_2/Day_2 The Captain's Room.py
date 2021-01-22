# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
noofrooms = input().split()
noofrooms.sort()
captroom = (set(noofrooms[0::2]) ^ set(noofrooms[1::2]))
print(captroom.pop())
