import json

def carregar_dados(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)

dados = carregar_dados("dados/exemplo.json")

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
    elif escolha == "3":
        print(dados["comercial"]["pergunta"])
        for opcao, info in dados["comercial"][ "opcoes"].items():                      
            print(f"{opcao}. {info['nome']}")
        resposta = input("> ")
        if resposta in dados ["comercial"][ "opcoes"]:                         
            setor = dados["comercial"]["opcoes"][resposta]["setor"]                              
            print(dados["mensagens"]["transferindo"].format(setor=setor))
            print(f"🔔 [TRANSFERIR → {setor}]")
        else:
            print(dados["mensagens"]["passar_para_humano"])
            print("🔔 [TRANSFERIR → Comercial]")
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



