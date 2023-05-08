# faça um programa que receba 3 notas de um aluno e diga se ele está aprovado, reprovado ou em recuperação, levando em consideração que a média de aprovação é 7,0.
media_escola = 7
nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota"))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("aluno aprovado!")
elif media >= 4:
    print("aluno em recuperação!")
else:
    print("aluno reprovado!")