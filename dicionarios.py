n = int(input())   ###O número dado
dict = []          ### Criando um dic 
for i in range(0,n):
    dict.append(str(input().strip()))
word = input()

letras1 = [] ###Uma lista de letras
count1 = 0
for i in range(len(word)):
    letras1.append(word[i])
    count1 = count1 + 1

for i in range(len(dict)):
    count2 = 0
    word2 = dict[i]
    if len(word2) == len(word):
        for c in range(len(word2)):
            if word2[c] in letras1:
                count2 = count2 + 1
        if count2/count1 >= 0.7:
            print(word2)
