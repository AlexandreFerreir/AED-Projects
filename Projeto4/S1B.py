import timeit
import random

class ChatNode:
    def __init__(self, chatId, username):
        self.chatId = chatId
        self.username = username
        self.prompts = []

    def add_prompt(self, prompt):
        self.prompts.append(prompt)

    def __lt__(self, other):
        return self.chatId < other.chatId
    def __le__(self, other):
        return self.chatId <= other.chatId
    def __gt__(self, other):
        return self.chatId > other.chatId
    def __ge__(self, other):
        return self.chatId >= other.chatId



class ChatSystemHEAP:
    def __init__(self):
        self.chats = []
        self.rotacoes = 0


    def new_prompt(self, chatId, username, prompt):
        for chat in self.chats:
            if chat.chatId == chatId:
                chat.add_prompt(prompt)
                #print("CHAT {} ATUALIZADO".format(chatId))
                return
        chat = ChatNode(chatId, username)
        chat.add_prompt(prompt)
        self.insertNode(self.chats, chat)
        #print("CHAT {} CRIADO".format(chatId))


    def get_chat(self, chatId):
        for chat in self.chats:
            if chat.chatId == chatId:
                #print(chat.username)
                for prompt in chat.prompts:
                    x=1
                    #print(prompt)
                #print("FIM")
                return
        #print("CHAT {} NAO ENCONTRADO".format(chatId))

    def delete_chat(self, chatId):
        for i, chat in enumerate(self.chats):
            if chat.chatId == chatId:
                self.deleteNode(self.chats, chat)
                #print("CHAT {} APAGADO".format(chatId))
                return
        #print("CHAT {} NAO ENCONTRADO".format(chatId))


    def heapify(self,array, n, i):

        largest = i
        l = 2 * i
        r = 2 * i + 1

        if l < n and array[i] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.rotacoes+=1
            self.heapify(array, n, largest)


    def insertNode(self,array, newNode):

        size = len(array)
        if size == 0:
            array.append(newNode)
        else:
            array.append(newNode)
            for i in range((size // 2) - 1, 0, -1):
                self.heapify(array, size, i)


    def deleteNode(self,array, Node):

        size = len(array)
        i = 0
        for i in range(0, size):
            if Node == array[i]:
                break

        array[i], array[size - 1] = array[size - 1], array[i]
        self.rotacoes+=1

        array.remove(Node)

        for i in range((len(array) // 2) - 1, 0, -1):
            self.heapify(array, len(array), i)

apoio=[0.1,0.9]
for i in range(2):
    percentagem = apoio[i]
    for j in range(1,6):
        chat_system = ChatSystemHEAP()
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

            command=lista[h]

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

        print("------------\nNºentradas: {}\n% inserções: {}\nTempo: {} s\n------------\nRotações: {}".format(N,percentagem,sum_time,chat_system.rotacoes))