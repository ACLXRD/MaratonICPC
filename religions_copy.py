counter=1
while True:
    n, m = [int(i) for i in input().split()]
    if n == 0:
        break
    u = set({stdnt for stdnt in range(1,n+1)})
    religions = []
    for k in range(m):
        i, j = [int(l) for l in input().split()]