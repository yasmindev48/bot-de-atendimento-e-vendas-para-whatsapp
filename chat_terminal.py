from bot.fluxo import carregar_dados, decidir_escolha

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
    acao, setor = decidir_escolha(escolha, dados)

    if acao == "encerrar":
        print(dados["mensagens"]["despedida"].format(nome=nome))
        break
    elif acao == "comercial":
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
    elif acao == "encaminhar":
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



