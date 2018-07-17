lista = list()
lista.append(0)
for i in range(5):
	aux = int(input())
	for j in range(len(lista)):
		if aux <= lista[j]:
			lista.insert(j,aux)
			break
		else:
			if j==len(lista)-1:
				lista.insert(j,aux)
lista.remove(lista[len(lista)-1])
print(lista)