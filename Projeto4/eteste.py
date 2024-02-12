import timeit
import random
class TopicNode:
    def __init__(self, topic):
        self.topic = topic
        self.count = 0
        self.left = None
        self.right = None


class TopicSystem:
    def __init__(self):
        self.root = None
        self.contador_topicos=0

    def add_subject(self, topic):
        node = self.find_node(topic)
        if node is None:
            new_node = TopicNode(topic)
            self.root = self.insert_node(self.root, new_node)
            new_node.count += 1
            self.contador_topicos+=1
            #print("REGISTADO")
        else:
            node.count += 1
            #print("REGISTADO")

    def get_subject_count(self, topic):
        node = self.find_node(topic)
        '''''
        if node is None:
            print("SUBJECT NAO ENCONTRADO")
        else:
            print(f"{node.topic} {node.count}")
        '''''
    def list_all(self):
        self.traverse_inorder(self.root)
        #print("FIM")

    def insert_node(self, root, new_node):
        if root is None:
            return new_node

        if new_node.topic < root.topic:
            root.left = self.insert_node(root.left, new_node)
        elif new_node.topic > root.topic:
            root.right = self.insert_node(root.right, new_node)

        return root

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            #print(f"{node.topic} {node.count}")
            self.traverse_inorder(node.right)

    def find_node(self, topic):
        current = self.root
        while current is not None:
            if topic < current.topic:
                current = current.left
            elif topic > current.topic:
                current = current.right
            else:
                return current
        return None

'''''
topic_system = TopicSystem()

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

for j in range(1,6):
    topic_system = TopicSystem()
    N=20000*j
    consola = ["GET_SUBJECT_COUNT", "LIST_ALL"]

    lista = []
    contador_gets=0
    sum_time=0
    total_topicos=0.2*N

    for j in range(int(total_topicos)):
        topico = "topico"
        n = random.randint(1, N)
        topico = topico + str(n)
        lista += ["ADD_SUBJECT {}".format(topico)]

    max_acessos = 0.9 * (0.05 * topic_system.contador_topicos)
    for i in range(int(N-total_topicos)):
        topico = "topico"
        indice = random.randint(0, 1)
        if(indice==0):
            if contador_gets<max_acessos:
                n = random.randint(1, N)
                topico = topico + str(n)
                lista += ["{} {} ".format(consola[indice], topico)]
                contador_gets+=1
        elif(indice==1):
            lista += [consola[indice]]

    lista+=["FIM"]
    h=0
    command=" "
    while(command[0]!="FIM"):

        command=lista[h]

        command = command.split(" ")
        if command[0] == "ADD_SUBJECT":
            start = timeit.default_timer()
            topic_system.add_subject(command[1])
            time = timeit.default_timer() - start
            sum_time += time

        if command[0] == "GET_SUBJECT_COUNT":
            start = timeit.default_timer()
            topic_system.get_subject_count(command[1])
            time = timeit.default_timer() - start
            sum_time += time



        if command[0] == "LIST_ALL":
            start = timeit.default_timer()
            topic_system.list_all()
            time = timeit.default_timer() - start

            sum_time += time

        h+=1

    print("------------\nNºentradas: {}\nTempo: {} s\n------------\nRotações: {}".format(N,sum_time,0))