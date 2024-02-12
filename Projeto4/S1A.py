import timeit
import random

class ChatNode:
    def __init__(self, chat_id, username):
        self.chat_id = chat_id
        self.username = username
        self.prompts = []
        self.left = None
        self.right = None

class ChatSystem:
    def __init__(self):
        self.root = None
        self.mensagem=None


    def new_prompt(self, chat_id, username, prompt):
        node = self.find_node(chat_id)
        if node is None:
            new_node = ChatNode(chat_id, username)
            new_node.prompts.append(prompt)
            self.root = self.insert_node(self.root, new_node)
            #print(f"CHAT {chat_id} CRIADO")
        else:
            node.prompts.append(prompt)
            #print(f"CHAT {chat_id} ATUALIZADO")

    def get_chat(self, chat_id):
        node = self.find_node(chat_id)
        '''''
        if node is None:
            print(f"CHAT {chat_id} NAO ENCONTRADO")
        else:
            print(node.username)
            for prompt in node.prompts:
                print(prompt)
            print("FIM")
        '''
    def delete_chat(self, chat_id):
        self.mensagem=None
        self.root = (self.remove_node(self.root, chat_id))
        #print(self.mensagem[0:4]+ " " +str(chat_id)+ " " +self.mensagem[5:])



    def insert_node(self, root, new_node):
        if root is None:
            return new_node

        if new_node.chat_id < root.chat_id:
            root.left = self.insert_node(root.left, new_node)
        elif new_node.chat_id > root.chat_id:
            root.right = self.insert_node(root.right, new_node)

        return root


    def remove_node(self, root, chat_id):
        if root is None:
            self.mensagem= "CHAT NAO ENCONTRADO"
            return None

        if chat_id < root.chat_id:
            root.left = self.remove_node(root.left, chat_id)
        elif chat_id > root.chat_id:
            root.right = self.remove_node(root.right, chat_id)
        else:
            if root.left is None:
                temp = root.right
                root = None
                self.mensagem = "CHAT APAGADO"
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                self.mensagem = "CHAT APAGADO"
                return temp

            temp = self.get_min_node_right(root.right)
            root.chat_id = temp.chat_id
            root.username = temp.username
            root.prompts = temp.prompts
            root.right = self.remove_node(root.right, temp.chat_id)

        return root
    def get_min_node_right(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_node(self, chat_id):
        current = self.root
        while current is not None:
            if chat_id < current.chat_id:
                current = current.left
            elif chat_id > current.chat_id:
                current = current.right
            else:
                return current
        return None

apoio=[0.1,0.9]
for i in range(2):
    percentagem = apoio[i]
    for j in range(1,6):
        chat_system = ChatSystem()
        N=20000*j
        consola = ["NEW_PROMPT", "GET_CHAT", "DELETE_CHAT"]

        user = "user"
        lista = []
        contador_insercoes=0
        sum_time=0
        max_insercoes=percentagem*N
        for i in range(N):
            prompt = "prompt"
            if(contador_insercoes<max_insercoes):
                indice=random.randint(0,2)
            else:
                indice = random.randint(1, 2)
            if(indice==0):
                n=random.randint(1,N)
                contador_insercoes+=1
                name=user+str(n)
                prompt=prompt+str(n)
                lista+=["{} {} {} {}".format(consola[indice],n,name,prompt)]

            elif(indice==1):
                n = random.randint(1, N)
                lista += ["{} {} ".format(consola[indice], n)]
            elif(indice==2):
                n = random.randint(1, N)
                lista += ["{} {}".format(consola[indice], n)]

        lista+=["FIM"]
        h=0
        command=" "
        while(command[0]!="FIM"):
            #comando = input()
            command=lista[h]
            #print(comando)
            command = command.split(" ")
            if command[0] == "NEW_PROMPT":
                start = timeit.default_timer()
                chat_system.new_prompt(int(command[1]), command[2], " ".join(command[3:]))
                time = timeit.default_timer() - start
                sum_time += time
            elif command[0] == "GET_CHAT":
                start = timeit.default_timer()
                chat_system.get_chat(int(command[1]))
                time = timeit.default_timer() - start
                sum_time += time


            elif command[0] == "DELETE_CHAT":
                start = timeit.default_timer()
                chat_system.delete_chat(int(command[1]))
                time = timeit.default_timer() - start

                sum_time += time
            h+=1

        print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\n------------\nRotações: {}".format(N,percentagem,sum_time,0))