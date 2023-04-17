nomes=['João Pedro','Humberto','Uchôa','Remerson','Paulo']
print(nomes)
print("Aqui vai a sequencia por ordem da lista acima:")
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[3])

#LISTA DE FRUTAS

frutas = ['pêra','uva','maçã','kiwi']
print(frutas)

#SUBSTITUINDO FRUTA DE ÍNDICE 1 PELA REQUERIDA
frutas[1] = 'abacate'
print(frutas)

frutas.insert(2,'morango')
print(frutas)
del frutas[4]
print(frutas)
#COMANDO INDEX E DEL
frutas.insert(5,'melancia')
print(frutas)
print(f'O index de frutas.index {frutas.index("melancia")}')
del frutas[frutas.index('melancia')]
print(frutas)
