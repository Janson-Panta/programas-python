#crie um código que calcule a área do retângulo e do triângulo.
while True:
    itens = input(" o que deseja calcular? 1 = triângulo    2 = retângulo   3 = encerrar")
    if itens == "1":
        base = float(input("digite a base do triângulo"))
        altura = float(input("digite a altura do triângulo"))
        área_triangulo = (base * altura) / 2
        print(f"A área do triângulo é {área_triangulo:.2f}")
    elif itens == "2":
        base = float(input("digite a base do retângulo"))
        altura = float(input("digite a altura do retângulo"))
        área_retângulo = (base * altura)
        print(f"A área do retângulo é {área_retângulo:.2f}")
    elif itens == "3":
        break
    else:
        print("opção inválida.")
        continue
    denovo = input("deseja fazer outro cálculo?  1 = sim    2 = não")
    if denovo == '1':
        print("vamos lá")
    else:
        break
