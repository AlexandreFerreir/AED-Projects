import random
import timeit

N = 20000
registos_aleatorios = []
def consulta_bd(listainformacao):
    listaordenada = listainformacao
    contador=0
    #start = timeit.default_timer()
    for i in range(1, len(listaordenada)):
        j = i
        while j > 0 and listaordenada[j][0] < listaordenada[j - 1][0]:
            listaordenada[j], listaordenada[j - 1] = listaordenada[j - 1], listaordenada[j]
            contador+=1
            j -= 1
    print(contador)
    #end = timeit.default_timer()
    #print(end - start)
    # print_lista(listaordenada)


for i in range(N):
    letras = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    numeros1 = "".join(random.choices('0123456789', k=2))
    numeros2 = "".join(random.choices('0123456789', k=2))
    tipo_linha = random.choice(['traco continuo', 'pneus nao homologados', 'excesso velocidade', 'busina avariada', 'pneus carecas', 'alcool','luzes fundidas'])
    comprimento = random.randint(1, 10)
    nome = ' '.join(random.choices(['Gabriela', 'Anabela', 'Carlos', 'Catarina', 'David', 'Alice', 'Liliana', 'Cilio', 'Fernanda', 'Belmira'],k=2))
    registos_aleatorios.append(f'{numeros1}{letras}{numeros2}{" "}{tipo_linha} {comprimento} {nome}')

def print_lista(lista):
    for i in range(len(lista)):
        print("".join(lista[i]))
    print("FIM")


def dim_bd(n, listainformacao):
    for i in range(n):
        listainformacao.append(input().split())
    return "BD_ATUALIZADA"


def consulta_matricula(matricula, listainformacao):
    contador = 0
    for i in range(len(listainformacao)):
        if listainformacao[i][0] == matricula:
            print(" ".join(listainformacao[i][1:]))
            contador += 1
    if contador == 0:
        print("REGISTOS NAO ENCONTRADOS\nFIM")
    else:
        print("FIM")


def consulta_condutor(nome, apelido, listainformacao):
    contador = 0
    for i in range(len(listainformacao)):
        if listainformacao[i][-2] == nome and listainformacao[i][-1] == apelido:
            print(" ".join(listainformacao[i][:-2]))
            contador += 1
    if contador == 0:
        print("REGISTOS NAO ENCONTRADOS\nFIM")
    else:
        print("FIM")



registos_aleatorios.sort(reverse=True)
listainformacao = registos_aleatorios
while 1:
    cmd = input().split()
    if cmd[0] == "DIM_BD":
        print(dim_bd(int(cmd[1]), listainformacao))

    elif cmd[0] == "CONSULTA_MATRICULA":
        consulta_matricula(cmd[1], listainformacao)

    elif cmd[0] == "CONSULTA_CONDUTOR":
        consulta_condutor(cmd[1], cmd[2], listainformacao)

    elif cmd[0] == "CONSULTA_BD":
        consulta_bd(listainformacao)
    else:
        break
