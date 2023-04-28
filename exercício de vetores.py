#solicite o tamanho de 2 vetores, em seguida solicite o preenchimento desses vetores e por ultimo some e coloque num terceiro vetor
tamanho = int(input("digite o tamanho dos vetores"))
lista1 = []
lista2 = []
lista3 = []
for x in range (tamanho):
    lista1.append(int(input("digite os valores para a primeira lista")))
for y in range (tamanho):
    lista2.append(int(input("digite os valores para a segunda lista")))
for j in range(tamanho):
    lista3.append(lista1[j] + lista2[j])
print(lista1)
print(lista2)
print(lista3)




