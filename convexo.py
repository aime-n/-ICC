n = int(input())

def det(a,b,c):
    deter = 0
    deter = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    deter -= (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
    return deter


vetores = []
for i in range(n):
    vetores.append(list(map(int,input().split())))
flag = det(vetores[0], vetores[1],vetores[2])
for i in range(n-2):
    if det(vetores[i], vetores[i+1],vetores[i+2]) * flag < 0:
        print('NAO CONVEXO')
        break
else:
    if det(vetores[n-2],vetores[n-1],vetores[0])*flag<0:
        print('NAO CONVEXO')
    elif det(vetores[n-1],vetores[0],vetores[1])*flag<0:
        print('NAO CONVEXO')
    else:
        print('CONVEXO')
