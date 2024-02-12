import random

N = int(input("Digite o valor de N: "))
percent_new_prompt = int(input("Digite a percentagem de comandos NEW_PROMPT: "))

# Gera uma lista aleatória de chatId's
chat_ids = random.sample(range(1, N+1), N)

commands = ["GET_CHAT", "DELETE_CHAT"]
weights = [1, 1]
if percent_new_prompt > 0:
    commands.append("NEW_PROMPT")
    weights.append(percent_new_prompt)

with open("inputrelatorio.txt", "w") as file:
    for chat_id in chat_ids:
        username = "user" + str(chat_id)
        prompt = "prompt" + str(chat_id)
        command = random.choices(commands, weights=weights)[0]
        if command == "NEW_PROMPT":
            file.write(f"NEW_PROMPT {chat_id} {username} {prompt}\n")
        else:
            file.write(f"{command} {chat_id}\n")

    file.write("FIM\n")
