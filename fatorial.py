###FATORIAL!
n = int(input())

# f = 1
# for i in range(1,n+1):
#     f = int(i)*f
#
# print(f)

# 
# def fatorial(n):
#     for i in range(1,n+1):
#         f = int(i)*f
#     return f

def fatorial(n):
    if n<2:
        return 1
    return n*fatorial(n-1)

print(fatorial(n))

###FORMULA: N * (N-1) * (N-2) * ... * 1
