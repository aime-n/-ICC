x = int(input())
# l = str(x)
# while x != 1:
#     if x % 2 == 0:
#         x = x/2
#     else:
#         x = x*3 + 1
#     l = l + " " + str(int(x))
# print(l)

def collatz(x):
    # print(x, end = " ")

    if x == 2:
        return 1
    elif x % 2 == 0:
        x = x/2
    else:
        x = x*3 + 1
    return collatz(int(x))

print(collatz(x))
#Grande 
#Aimê
