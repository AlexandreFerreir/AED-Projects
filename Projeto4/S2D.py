import timeit
import random
class UserNode:
    def __init__(self, username, plan):
        self.username = username
        self.plan = plan
        self.left = None
        self.right = None
        self.height = 1


class UserSystemAVL:
    def __init__(self):
        self.root = None
        self.message = None
        self.rotacoes=0

    def new_user(self, username, plan):
        node = self.find_node(username)
        if node is None:
            new_node = UserNode(username, plan)
            self.root = self.insert_node(self.root, new_node)
            #print(f"USER {username} CRIADO")
        else:
            #print(f"USER {username} JA EXISTE")
            x=1

    def update_user(self, username, plan):
        node = self.find_node(username)
        if node is None:
            #print("USER NAO ENCONTRADO")
            x=1
        else:
            node.plan = plan
            #print(f"USER {username} ATUALIZADO")

    def get_type(self, username):
        node = self.find_node(username)
        '''''
        if node is None:
            print("USER NAO ENCONTRADO")
        else:
            print(node.plan)
        '''
    def delete_user(self, username):
        node = self.find_node(username)
        if node is None:
            #print("USER NAO ENCONTRADO")
            x=1
        else:
            self.root = self.remove_node(self.root, username)
            #print(f"USER {username} APAGADO")

    def insert_node(self, root, new_node):
        if root is None:
            return new_node

        if new_node.username < root.username:
            root.left = self.insert_node(root.left, new_node)
        elif new_node.username > root.username:
            root.right = self.insert_node(root.right, new_node)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # LL
        if balance > 1 and new_node.username < root.left.username:
            return self.right_rotate(root)

        # RR
        if balance < -1 and new_node.username > root.right.username:
            return self.left_rotate(root)

        # LR
        if balance > 1 and new_node.username > root.left.username:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and new_node.username < root.right.username:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def remove_node(self, root, username):
        if root is None:
            return None

        if username < root.username:
            root.left = self.remove_node(root.left, username)
        elif username > root.username:
            root.right = self.remove_node(root.right, username)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_node_right(root.right)
            root.username = temp.username
            root.plan = temp.plan
            root.right = self.remove_node(root.right, temp.username)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_node_right(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, node):
        self.rotacoes+=1
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def right_rotate(self, node):
        self.rotacoes += 1
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def find_node(self, username):
        current = self.root
        while current is not None:
            if current.username == username:
                return current
            elif username < current.username:
                current = current.left
            else:
                current = current.right
        return None

''''
user_system = UserSystemAVL()

while True:
    command = input().split()
    if command[0] == "NEW_USER":
        user_system.new_user(command[1], command[2])
    elif command[0] == "UPDATE_USER":
        user_system.update_user(command[1], command[2])
    elif command[0] == "GET_TYPE":
        user_system.get_type(command[1])
    elif command[0] == "DELETE_USER":
        user_system.delete_user(command[1])
    elif command[0] == "FIM":
        break
        
'''
apoio = [0.1, 0.9]
for i in range(2):
    percentagem = apoio[i]
    for j in range(1, 6):
        user_system = UserSystemAVL()
        N = 200000 * j
        consola = ["NEW_USER", "UPDATE_USER", "GET_TYPE", "DELETE_USER"]
        planos = ["FREE", "BASIC", "PREMIUM"]
        user = "user"
        lista = []
        contador_insercoes = 0
        sum_time = 0
        max_insercoes = percentagem * N
        for i in range(N):
            if (contador_insercoes < max_insercoes):
                indice = random.randint(0, 3)
            else:
                indice = random.randint(1, 3)
            if (indice == 0):
                contador_insercoes += 1
                name = user + str(random.randint(1, N))
                lista += ["{} {} {}".format(consola[indice], name, planos[random.randint(0, 2)])]
            elif (indice == 1):
                name = user + str(random.randint(1, N))
                lista += ["{} {} {}".format(consola[indice], name, planos[random.randint(0, 2)])]
            elif (indice == 2):
                name = user + str(random.randint(1, N))
                lista += ["{} {}".format(consola[indice], name)]
            elif (indice == 3):
                name = user + str(random.randint(1, N))
                lista += ["{} {}".format(consola[indice], name)]
        lista += ["FIM"]
        h = 0
        command = " "
        while (command[0] != "FIM"):
            command = lista[h]
            command = command.split(" ")
            if command[0] == "NEW_USER":
                start = timeit.default_timer()
                user_system.new_user(command[1], command[2])
                time = timeit.default_timer() - start
                sum_time += time
            elif command[0] == "UPDATE_USER":
                start = timeit.default_timer()
                user_system.update_user(command[1], command[2])
                time = timeit.default_timer() - start
                sum_time += time

            elif command[0] == "GET_TYPE":
                start = timeit.default_timer()
                user_system.get_type(command[1])
                time = timeit.default_timer() - start
                sum_time += time


            elif command[0] == "DELETE_USER":
                start = timeit.default_timer()
                user_system.delete_user(command[1])
                time = timeit.default_timer() - start

                sum_time += time
            h += 1

        print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\n------------\nRotações: {}".format(N,
                                                                                                              percentagem,sum_time, user_system.rotacoes))
