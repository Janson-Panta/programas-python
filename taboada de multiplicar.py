# crie um programa para ler um número de 1 a 9 e em seguida gere a taboada de multiplicação desse número.
valor = int(input("digite um número de 1 à 9"))
if valor >= 1 and valor <= 9:
    for x in range (1,10):
        print(valor,"*",x,"=",valor*x)
else:
    print("digite apenas valores de 1 à 9")