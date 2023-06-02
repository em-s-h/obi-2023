# Primeiro criamos uma variável para guardar a quantidade
# de lances feitos.
numero_lances = int(input())

# Depois disso criamos 2 vetores, um para guardar os nomes
# dos lancers e outro para guardar os valores dos lances.
nomes = []
valores = []

# E por último criamos as variáveis que irão conter o maior
# lance e o vencedor.
maior_lance = 0
vencedor = 0

# Agora recebemos os dados dos lances e adicionamos eles
# aos seus respectivos vetores.
for i in range(numero_lances):
    nomes.append(input())
    valores.append(int(input()))

# Depois disso nós comparamos os valores dos lances.
for indice in range(0, len(valores)):
    # Variável temporaria utilizada para guardar o valor
    # do próximo lance a ser comparado.
    tmp = valores[indice] 

    # Comparamos o valor do maior lance até agora com o
    # valor do próximo lance, se o maior lance for menor
    # nós guardamos o valor da variável temporaria na
    # variável de maior lance.
    if (maior_lance < tmp):
        maior_lance = tmp
        vencedor = nomes[indice]

# Por fim imprimimos o nome do vencedor juntamente ao
# valor de seu lance.
print(vencedor)
print(maior_lance)
