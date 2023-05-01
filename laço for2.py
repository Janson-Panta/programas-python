# faça um programa que receba o nome de uma pessoa e imprima na tela letra por letra e ao lado de cada letra o número de posição.
nome = input("qual o seu nome?")
conta_letras = 0
for x in nome:
    conta_letras += 1
    print(x,conta_letras)
