#crie um programa que leia a quantidade de alunos em uma sala, em seguida leia os nomes de cada um e por fim crie um sistema de busca pelo nome do aluno.
quantidade = int(input("qual o numero de alunos?"))
lista_alunos = []
for x in range (1,quantidade+1):
    lista_alunos.append(input("digite o nome dos alunos"))
print(f"sua lista de alunos é: {lista_alunos}")
procurar_aluno = input("deseja procurar por um aluno na lista?  1 = sim   2 = não")
if procurar_aluno == "1":
    nome_aluno = input("qual aluno?")
    if nome_aluno in lista_alunos:
        print(f"o aluno está na lista na posição {lista_alunos.index(nome_aluno)+1}")
    else:
        print("o aluno não está na lista")
else:
    print("okay")
