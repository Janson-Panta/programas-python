# Crie um programa que receba a quantidade de alunos em uma sala e após isso, coloque o nome de cada um dentro de uma lista.

quantidade_alunos = int(input("quantos alunos tem na sala?"))
lista_alunos = []
for x in range (1,quantidade_alunos+1):
    lista_alunos.append(input("digite o nome de cada um deles"))
print(f"aqui está sua lista de alunos:  {lista_alunos}")