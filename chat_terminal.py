import json

with open("dados/exemplo.json", encoding="utf-8") as f:
    dados = json.load(f)

print(dados["mensagens"]["saudacao"])
print(dados["mensagens"]["pedir_nome"])
nome = input(">")
print(dados["mensagens"]["apresentar_menu"].format(nome=nome))
print()
for opcao, info in dados["menu"].items():
    print(f"{opcao}. {info['nome']}")

print()
tentativas = 0

while True:
    escolha = input(">")

    if escolha == "0":
        print(dados["mensagens"]["despedida"].format(nome=nome))
        break
    elif escolha in dados["menu"]:
        setor = dados["menu"][escolha]["setor"]
        print(dados["mensagens"]["transferindo"].format(setor=setor))
        print(f"🔔 [TRANSFERIR → {setor}]")
        break
    else:
        tentativas +=1
        if tentativas == 2:
            print(dados["mensagens"]["passar_para_humano"])
            print("🔔 [TRANSFERIR → Comercial]")
            break
        print(dados["mensagens"]["nao_entendi"])



