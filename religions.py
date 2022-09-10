counter=1
while True:
    n, m = [int(i) for i in input().split()]
    if (n, m) == (0,0):
        break
    u = set({stdnt for stdnt in range(1,n+1)})
    religions = []
    for k in range(m):
        i, j = [int(l) for l in input().split()]
        for idx in range(len(religions)):
            r = religions[idx]
            if i in r or j in r:
                P = {i,j}
                r = r.union(P)
                try: 
                    u.remove(i)
                except:
                    pass
                try:
                    u.remove(j)
                except:
                    pass
                religions[idx] = r
                break
        else:
            religions.append({i,j})
            try: 
                u.remove(i)
            except:
                pass
            try:
                u.remove(j)
            except:
                pass
    print(u)
    print(f"Case {counter}: {len(religions)+int(len(u)>0)*len(u)}")
    counter+=1
