n,r = list(map(int,input().split()))

def diam(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return diam(n-1) + diam(n-2)

d = diam(20)

def raio(a,b,c):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    x3, y3 = c[0], c[1]

    A = x1*(y2 - y3) - y1*(x2 - x3) + x2*y3 - x3*y2
    B = (x1**2 + y1**2)*(y3 - y2) + (x2**2 + y2**2)*(y1 - y3) + (x3**2 + y3**2)*(y2 - y1)
    C = (x1**2 + y1**2)*(x2 - x3) + (x2**2 + y2**2)*(x3 - x1) + (x3**2 + y3**2)*(x1 - x2)

    if A != 0:
        x = (-1)*B/(2*A)
        y = (-1)*C/(2*A)
        return pow((x-x1)**2 + (y-y1)**2, 1/2)

vet = []
for i in range(n):
    vet.append(list(map(int,input().split())))

flag = 0
for i in vet:
    for j in vet[vet.index(i):]:
        for k in vet[vet.index(j):]:
            if raio(i,j,k) == r:
                flag = 1

if flag:
    print("S")
else:
    print("N")
# Circunferencia 
