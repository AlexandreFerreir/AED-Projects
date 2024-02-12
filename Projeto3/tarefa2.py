import random
import timeit

N = 60000
registos_aleatorios = []

for i in range(N):
    letras = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    numeros1 = "".join(random.choices('0123456789', k=2))
    numeros2 = "".join(random.choices('0123456789', k=2))
    tipo_linha = random.choice(['traco continuo', 'pneus nao homologados', 'excesso velocidade', 'busina avariada','pneus carecas','alcool','luzes fundidas'])
    comprimento = random.randint(1, 10)
    nome = ' '.join(random.choices(['Gabriela', 'Anabela', 'Carlos', 'Catarina', 'David', 'Alice', 'Liliana', 'Cilio', 'Fernanda', 'Belmira'], k=2))

    registos_aleatorios.append(f'{numeros1}{letras}{numeros2}{" "}{tipo_linha} {comprimento} {nome}'.split())

def print_lista(lista):
    for i in range(len(lista)):
        print("".join(lista[i][0]))
    print("FIM")


def dim_bd(n):
    for i in range(n):
        listainformacao.append(input().split())
    return "BD_ATUALIZADA"


def consulta_matricula(matricula):
    contador = 0
    for i in range(len(listainformacao)):
        if listainformacao[i][0][0] == matricula:
            print(" ".join(listainformacao[i][0][1:]))
            contador += 1
    if contador == 0:
        print("REGISTOS NAO ENCONTRADOS\nFIM")
    else:
        print("FIM")


def consulta_condutor(nome, apelido):
    contador = 0
    for i in range(len(listainformacao)):
        if listainformacao[i][0][-2] == nome and listainformacao[i][0][-1] == apelido:
            print(" ".join(listainformacao[i][0][:-2]))
            contador += 1
    if contador == 0:
        print("REGISTOS NAO ENCONTRADOS\nFIM")
    else:
        print("FIM")


def consulta_bd():
    listaindice = []
    contador=0
    gap = round(len(listainformacao) / 2.2)
    for i in range(len(listainformacao)):
        listaindice.append([listainformacao[i], i])
    #start = timeit.default_timer()
    while gap > 0:
        for i in range(gap, len(listaindice)):
            j = i
            while j >= gap:
                if listaindice[j - gap][0][0] > listaindice[j][0][0] or (listaindice[j - gap][0][0] == listaindice[j][0][0] and listaindice[j - gap][1] >listaindice[j][1]):
                    listaindice[j - gap], listaindice[j] = listaindice[j], listaindice[j - gap]
                    contador+=1
                    j -= gap
                else:
                    break
        gap = round(gap / 2.2)
    print(contador)
    #end = timeit.default_timer()
    #print(end - start)
    return listaindice


#registos_aleatorios.sort(reverse=True)
listainformacao = registos_aleatorios
ordenada=False
while 1:
    cmd = input().split()
    if cmd[0] == "DIM_BD":
        print(dim_bd(int(cmd[1])))

    elif cmd[0] == "CONSULTA_MATRICULA":
        consulta_matricula(cmd[1])

    elif cmd[0] == "CONSULTA_CONDUTOR":
        consulta_condutor(cmd[1], cmd[2])

    elif cmd[0] == "CONSULTA_BD":
        if ordenada==False:
            listainformacao=consulta_bd()
            ordenada=True

        #print_lista(listainformacao)

    else:
        break
