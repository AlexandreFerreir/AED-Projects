import timeit
import random


class TopicNode:
    def __init__(self, topic):
        self.topic = topic
        self.count = 0
        self.color = 1
        self.left = None
        self.right = None
        self.parent = None


class TopicSystemRB:
    def __init__(self):
        self.root = None
        self.rotacoes = 0
        #self.contador_topicos = 0

    def add_subject(self, topic):
        node = self.find_node(topic)
        if node is None:
            new_node = TopicNode(topic)
            self.root = self.insert_node(self.root, new_node)
            new_node.count += 1
            self.fix_insert(new_node)
            #self.contador_topicos += 1
            # print("REGISTADO")
        else:
            node.count += 1
            # print("REGISTADO")

    def get_subject_count(self, topic):
        node = self.find_node(topic)
        '''if node is None:
            #print("SUBJECT NAO ENCONTRADO")
        else:
            #print(f"{node.topic} {node.count}")
        '''

    def list_all(self):
        self.percorre_ordem(self.root)
        # print("FIM")

    def insert_node(self, root, new_node):
        if root is None:
            return new_node

        if new_node.topic < root.topic:
            root.left = self.insert_node(root.left, new_node)
            root.left.parent = root
        elif new_node.topic > root.topic:
            root.right = self.insert_node(root.right, new_node)
            root.right.parent = root

        return root

    def fix_insert(self, node):
        while node.parent is not None and node.parent.color == 1:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == 1:
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == 1:
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)

        self.root.color = 0

    def left_rotate(self, node):
        aux_node = node.right
        node.right = aux_node.left
        if aux_node.left is not None:
            aux_node.left.parent = node
        aux_node.parent = node.parent
        if node.parent is None:
            self.root = aux_node
        elif node == node.parent.left:
            node.parent.left = aux_node
        else:
            node.parent.right = aux_node
        aux_node.left = node
        node.parent = aux_node
        self.rotacoes += 1


    def right_rotate(self, node):
        aux_node = node.left
        node.left = aux_node.right
        if aux_node.right is not None:
            aux_node.right.parent = node
        aux_node.parent = node.parent
        if node.parent is None:
            self.root = aux_node
        elif node == node.parent.right:
            node.parent.right = aux_node
        else:
            node.parent.left = aux_node
        aux_node.right = node
        node.parent = aux_node

        self.rotacoes += 1

    def find_node(self, topic):
        current_node = self.root
        while current_node is not None:
            if topic == current_node.topic:
                return current_node
            elif topic < current_node.topic:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def percorre_ordem(self, node):
        if node is not None:
            self.percorre_ordem(node.left)
            # print(f"{node.topic} {node.count}")
            self.percorre_ordem(node.right)


'''topic_system = TopicSystemRB()

while True:
    command = input().split()
    if command[0] == "ADD_SUBJECT":
        topic_system.add_subject(command[1])
    elif command[0] == "GET_SUBJECT_COUNT":
        topic_system.get_subject_count(command[1])
    elif command[0] == "LIST_ALL":
        topic_system.list_all()
    elif command[0] == "FIM":
        break
'''
apoio = [0.7]
for i in range(1):
    percentagem = apoio[i]
    for j in range(1, 6):
        topic_system = TopicSystemRB()
        N = 20000 * j
        consola = ["ADD_SUBJECT", "GET_SUBJECT_COUNT", "LIST_ALL"]

        topico = "topico"
        lista = []
        contador_insercoes = 0
        sum_time = 0
        max_insercoes = percentagem * N
        for i in range(N):
            if (contador_insercoes < max_insercoes):
                indice = random.randint(0, 2)
            else:
                indice = random.randint(1, 2)
            if (indice == 0):
                contador_insercoes += 1
                name = topico + str(random.randint(1, N))
                lista += ["{} {} ".format(consola[indice], name)]
            elif (indice == 1):
                name = topico + str(random.randint(1, N))
                lista += ["{} {}".format(consola[indice], name)]
            elif (indice == 2):
                name = topico + str(random.randint(1, N))
                lista += ["{}".format(consola[indice])]
        lista += ["FIM"]
        h = 0
        command = " "
        while (command[0] != "FIM"):
            command = lista[h]
            command = command.split(" ")
            if command[0] == "ADD_SUBJECT":
                start = timeit.default_timer()
                topic_system.add_subject(command[1])
                time = timeit.default_timer() - start
                sum_time += time
            elif command[0] == "GET_SUBJECT_COUNT":
                start = timeit.default_timer()
                topic_system.get_subject_count(command[1])
                time = timeit.default_timer() - start
                sum_time += time

            elif command[0] == "LIST_ALL":
                start = timeit.default_timer()
                topic_system.list_all()
                time = timeit.default_timer() - start
                sum_time += time

            h += 1

        print("------------\nNºentradas: {}\nTempo: {} s\n------------\nRotações: {}".format(N,sum_time,topic_system.rotacoes))
