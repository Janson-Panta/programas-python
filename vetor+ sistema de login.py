# crie 2 vetores para que sejam preenchidos. após isso crie um sistema de login com esses vetores.
lista_nome = []
lista_senha = []
for x in range (2):
    lista_nome.append(input("digite um nome"))
    lista_senha.append(input("digite uma senha"))
print("efetue seu login!")
user = input("digite o usuário")
senha = input("digite a senha")
for y in range (2):
    if lista_nome[y] == user and lista_senha[y]== senha:
        print("login efetuado com sucesso")
        break
else:
    print("usuário ou senha incorretos!")

