# Primeiramente, criamos uma variável buffer de entrada "input_buffer".
#
# Um buffer de entrada contém os dados que entram em nosso programa
# enquanto nós movemos eles para o local desejado.
#
# Aqui usamos este buffer de entrada para executar uma simples operação
# de separar "split" na entrada, a razão para fazer isso é porque a
# primeira entrada que nosso programa recebe é um string como este "2 3",
#
# dois números separados por um espaço, sendo o primeiro a quantidade
# de tipos de roupas e o segundo a quantidade de tamanhos de roupas,
#
# para obter esses números, temos que separá-los em dois valores diferentes,
# o que pode ser obtido usando a função "split()" que retorna os valores
# separados em um vetor, armazenamos este vetor no buffer de entrada
# novamente para que possamos usá-lo mais tarde.
input_buffer = input()
input_buffer = input_buffer.split()

# Aqui só precisamos armazenar a quantidade de tipos de roupas já que o
# nosso programa não precisa da quantidade de tamanhos.
quant_tipos = int(input_buffer[0])
estoque = [] # Criar a variável que vai guardar o estoque.

# Neste loop 'for' obtemos a quantidade de roupas para cada tipo.
#
# Como a entrada que estamos recebendo também está no formato "1 2 3",
# fazemos a operação 'split' novamente.
for tipo in range(quant_tipos):
    input_buffer = input()
    quant_roupas = input_buffer.split()

    estoque.append(quant_roupas)

# Após este loop 'for' a variável 'estoque' ficará assim:
#
#   | Tamanho
# --|---------
# T | 1 2 3 x
# i | 4 5 6 x
# p | 7 8 9 x
# o | x x x x
#
# 'x' indica que pode haver mais números após os mostrados.

# Aqui recebemos a quantidade de pedidos feitos e criamos a variável
# que vai guardar o total de vendas feitas.
quant_pedidos = int(input())
total_vendas = 0

# Neste loop 'for', primeiro obtemos a ordem e, mais uma vez, chamamos
# a função 'split()', pois a entrada está neste formato '1 1'.
#
# Depois de separar os valores guardamos eles em suas respectivas variáveis
# para facilitar o seu uso depois, o motivo de diminuir 1 dos valores é
# porque os vetores usam um índice que começa com 0, então a ordem da
# roupa do tipo 1 e tamanho 1 estaria na posição 0 0.
for i in range(0, quant_pedidos):
    pedido = input()
    pedido = pedido.split()

    tipo = int(pedido[0]) - 1
    tamanho = int(pedido[1]) - 1

    # Neste 'if' verificamos se o item pedido está em estoque, se estiver
    # diminuímos a quantidade do item por 1 e como conseguimos vender o
    # item adicionamos 1 ao total das vendas efetuadas.
    if (int( estoque[tipo][tamanho] ) != 0):

        estoque[tipo][tamanho] = int( estoque[tipo][tamanho] ) - 1
        total_vendas += 1

# E por fim imprimimos o total de vendas realizadas.
print(total_vendas)
