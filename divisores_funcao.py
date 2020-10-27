n = int(input())

def divisores(n):
    d = []
    if n>=1:
        for i in range(2,n):
            if n%i == 0:
                d.append(int(i))
    if not d:
        return f"{n} eh primo"
    return d

print(divisores(n))
