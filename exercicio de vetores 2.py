# faça um código para ler 10 valores, em seguida ler um valor qualquer e dizer quantas vezes esse valor se repete no vetor.
vetor = []
for x in range (10):
    vetor.append(int(input("digite os valores")))
numero = int(input("digite um numero qualquer"))
conta = 0
for i in range (10):
    if vetor[i] == numero:
        conta += 1
print(f"o numero se repete {conta} vezes")

