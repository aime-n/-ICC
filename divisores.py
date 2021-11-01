n = input()
i = n

try:
    n = int(n)
    i = int(i)
    if n>=0:
        while i > 0:
            if n%i == 0:
                print(i)
            i -= 1
    else:
        print("Digite um número positivo.")
except:
    print("Digite um número inteiro.")

# função tosca
    
