#QUESTÃO 1
nome = ('João Pedro')
pessoa = {
    'primeiro_nome': (nome),
    'segundo_nome': 'Silva Souza Nunes',
    'idade': 23,
    'cidade':'João Pessoa'
}
print(f'Primeiro Nome: {pessoa["primeiro_nome"]}')
print(f'Segundo Nome: {pessoa["segundo_nome"]}')
print(f'Idade: {pessoa["idade"]}')
print(f'Cidade residente: {pessoa["cidade"]}')

#QUESTÃO 2

num_fav = {
    "JP":10,
    "JV":9,
    "HUMBERTO":20,
    "REMERSON":24,
    "PAULO":2,
}
for nome in num_fav.keys():
    print(f'{nome} -> {num_fav[nome]}')

#QUESTÃO 3
lista = [1,2,3,4,5,6]
print(lista)
soma = (lista[1] + lista[3] + lista[5])
print(soma)




