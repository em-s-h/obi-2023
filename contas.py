# Primeiro criamos a variável que vai conter o valor que Vô João tem
# disponível para pagar as contas
conta_do_vo = 0

# Depois criamos um vetor que vai conter os valores das três contas
# a serem pagas.
contas = [0, 0, 0]

# Aqui recebemos os valores das variáveis e convertemos o valor de 
# "string" para "int" (numero).
conta_do_vo = int(input())

contas[0] = int(input()) # Conta do Açougue.
contas[1] = int(input()) # Conta da Farmácia.
contas[2] = int(input()) # Conta da Padaria.

# Aqui nós ordenamos os valores do vetor de contas em ordem crescente.
# (Por isso nós criamos um vetor ao invés de 3 variáveis diferentes)
contas.sort()

# Auto-explicativo. Contém quantas contas João pode pagar.
contas_pagas = 0 

# Esta variável ira conter a soma das contas a serem pagas.
divida = 0

# Aqui fazemos um loop "for" que vai executar o codigo dentro de seu
# escopo para cada conta do vetor "contas".
#
# Neste loop for nós adicionamos a divida uma das contas, após isso
# verificamos se João consegue pagar esta divida, se ele conseguir
# adicionamos 1 ao total de contas que podem ser pagas.
for conta in range(0, len(contas)):
    divida += contas[conta]

    if ((conta_do_vo - divida) >= 0):
        contas_pagas += 1

# Após a execução do loop imprimimos quantas contas João consegue
# pagar.
print(contas_pagas)
