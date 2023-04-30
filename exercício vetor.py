# crie um programa que receba 5 valores, coloque dentro de um vetor e print em ordem invertida.
vetor = []
for x in range(5):
   vetor.append(int(input("digite os números")))
for j in range(4,-1,-1):
    print(vetor[j],end = "")


