# O programa inicia na linha 68

# Aqui definimos uma função que verifica se a sala atual está conectado a próxima sala,
# retornando 'True' se estiverem conectadas e 'False' caso contrário.
#
# Esta função possui 3 parâmetros:
# - 'atual' representa a sala atual;
# - 'proximo' representa a próxima sala;
# - 'tuneis' contém o vetor 'tuneis' definido em nosso programa.
def verificar_salas(atual, proximo, tuneis):
    # Primeiro, iniciamos um loop 'for' que percorrerá os valores do vetor 'tuneis'.
    for i in range(0, len(tuneis)):
        # Depois disso, verificamos se a sala atual se conecta a próxima sala,
        # fazemos isso usando um recurso do Python que nos permite verificar se um
        # vetor contém um determinado valor, fazemos isso para a versão normal do
        #
        # valor e a versão invertida do valor, isso é feito porque, por exemplo,
        # um túnel pode conectar da sala 5 à sala 2 e vice-versa, portanto,
        # poderia ser escrito assim "5 2" e assim "2 5".
        #
        # Se as salas estiverem conectadas 'True' é retornado.
        if f"{atual} {proximo}" in tuneis[i]:
            return True

        elif f"{proximo} {atual}" in tuneis[i]:
            return True
    
    # Se a sala atual e a próxima não puderem ser conectadas, o loop 'for' acima
    # terminará e 'False' será retornado.
    return False

# Aqui definimos uma função que verifica se o passeio é possível ou não, retornando
# 'True' se for possível e 'False' caso contrário.
#
# Esta função tem 2 parâmetros:
# - 'passeio' representa o passeio que foi sugerido; 
# - 'tuneis' contém o vetor 'tuneis' definido em nosso programa.
def verificar_passeio(passeio, tuneis):
    # Primeiro, iniciamos um loop 'for' que percorrerá os valores do vetor 'passeio'.
    for i in range(0, len(passeio)):
        # Depois fazemos uma verificação rápida para ver se a variável 'i' é o índice
        # do último segmento do vetor 'passeio', isso nos ajuda a evitar um erro de
        # índice fora dos limites, se 'i' for o índice do último segmento segmento,
        #
        # não precisamos verificar se a sala atual está conectada a outra sala, pois
        # é a última sala, portanto, saímos do loop.
        if (i == len(passeio) - 1):
            break;

        # Aqui armazenamos a sala atual e a próxima sala.
        sala_atual = passeio[i]
        prox_sala = passeio[i + 1]

        # Para que aqui possamos verificar se essas salas estão conectadas ou não
        # chamando nossa função 'verificar_salas()', guardamos também o valor de
        # retorno da função para uso posterior.
        estao_conectadas = verificar_salas(sala_atual, prox_sala, tuneis)

        # Aqui usamos o valor retornado da nossa função para sair do loop caso as
        # salas não estejam conectadas.
        if not estao_conectadas:
            return False

    # Se todas as salas do passeio sugerido estiverem conectadas umas às outras,
    # o loop 'for' acima será concluído e 'True' será retornado.
    return True

# Aqui fizemos a mesma coisa que a resposta anterior, então não há necessidade de
# explicar.
input_buffer = input()
input_buffer = input_buffer.split()

# Aqui armazenamos o número de túneis, pois é a única informação que precisamos da
# primeira entrada, e também criamos o vetor 'tuneis' que conterá as salas que estão
# conectadas ao respectivo túnel.
num_tuneis = int(input_buffer[1])
tuneis = []

# Depois disso, adicionamos os dados do túnel ao vetor 'tuneis'.
for i in range(num_tuneis):
    tuneis.append(input())

# Agora armazenamos o número de passeios sugeridos e também criamos a variável que
# armazenará quantos desses passeios sugeridos são realmente possíveis.
num_sujest_passeio = int(input())
passeios_possiveis = 0

for i in range(num_sujest_passeio):
    passeio = input()
    passeio = passeio.split()
    passeio.pop(0)

    passeio_e_possivel = verificar_passeio(passeio, tuneis)

    if passeio_e_possivel:
        passeios_possiveis += 1

# E por último imprimimos quantos passeios são possíveis.
print(passeios_possiveis)
