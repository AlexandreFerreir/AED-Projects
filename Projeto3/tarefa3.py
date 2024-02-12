import random
import timeit

N = 100000
registos_aleatorios = []
contador=0


for i in range(N):
    letras = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    numeros1 = "".join(random.choices('0123456789', k=2))
    numeros2 = "".join(random.choices('0123456789', k=2))
    tipo_linha = random.choice(['traco continuo', 'pneus nao homologados', 'excesso velocidade', 'busina avariada','pneus carecas','alcool','luzes fundidas'])
    comprimento = random.randint(1, 10)
    nome = ' '.join(random.choices(['Gabriela', 'Anabela', 'Carlos', 'Catarina', 'David', 'Alice', 'Liliana', 'Cilio', 'Fernanda', 'Belmira'], k=2))

    registos_aleatorios.append(f'{numeros1}{letras}{numeros2}{" "}{tipo_linha} {comprimento} {nome}'.split())

#print(registos_aleatorios)

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


def consulta_bd(listaorganizada):
    global contador
    if len(listaorganizada) <= 1:
        return listaorganizada
    else:
        pivot = [[listaorganizada[0], 0], [listaorganizada[len(listaorganizada) // 2], len(listaorganizada) // 2],
                 [listaorganizada[-1], len(listaorganizada) - 1]]
        pivot.sort(key=lambda x: x[0])
        indx_pivot = pivot[1][1]
        pivot = pivot[1][0]
        smaller, greater = [], []


        for indx, val in enumerate(listaorganizada):
            if indx != indx_pivot:
                if val[0] < pivot[0]:
                    if(indx>indx_pivot):
                        contador += 1
                    smaller.append(val)

                elif val[0] > pivot[0]:
                    greater.append(val)
                    if (indx < indx_pivot):
                        contador += 1


                else:
                    if indx < indx_pivot:
                        smaller.append(val)


                    else:
                        greater.append(val)
                        contador += 1


        return consulta_bd(smaller) + [pivot] + consulta_bd(greater)


registos_aleatorios.sort(reverse=True)
#print(registos_aleatorios)
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
        #start = timeit.default_timer()

        listainformacao = consulta_bd(listainformacao)
        print(contador)
        #end = timeit.default_timer()
        #print(end - start)
        #print_lista(listainformacao)
    else:
        break
