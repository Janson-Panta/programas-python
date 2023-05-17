#crie uma função que mostre na tela um texto ao contrário.
def textocontra():
    vetor = []
    frase = input("digite uma frase")
    for x in range(len(frase)):
        vetor.append(frase[x])
    for y in range(len(vetor)- 1, -1, -1):
        print(vetor[y],end = " ")


textoconta()
