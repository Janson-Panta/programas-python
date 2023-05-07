# crie um programa para ler 2 números, efetuar as 4 operações matemáticas e mostrar o resultado.
numero1 = int(input("digite o primeiro número"))
numero2 = int(input("digite o segundo número"))
while True:
    operacao = input("qual operação deseja realizar? 1 = adição  2 = subtração  3 = divisão  4 = multiplicação")
    if operacao == "1":
        print(numero1 + numero2)
        break
    elif operacao == "2":
        print(numero1 - numero2)
        break
    elif operacao == "3":
        print(numero1 / numero2)
        break
    elif operacao == "4":
        print(numero1 * numero2)
        break
    else:
        print("digite uma opção válida")
        continue

