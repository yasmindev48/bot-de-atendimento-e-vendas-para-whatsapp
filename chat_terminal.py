from bot.handoff import deve_passar_para_humano
from bot.fluxo import carregar_dados, decidir_escolha, decidir_comercial

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
        acao_comercial, setor = decidir_comercial(resposta, dados)
        if acao_comercial == "encaminhar":
            destino = dados["comercial"]["opcoes"][resposta]["destino"]
            print(dados["mensagens"]["transferindo"].format(destino=destino))
            print(f"🔔 [TRANSFERIR → {setor}]")
        else:
            print(dados["mensagens"]["passar_para_humano"])
            print(f"🔔 [TRANSFERIR → {setor}]")
        break
    elif acao == "encaminhar":
        destino = dados["menu"][escolha]["destino"]
        print(dados["mensagens"]["transferindo"].format(destino=destino))
        print(f"🔔 [TRANSFERIR → {setor}]")
        break
    else:
        tentativas +=1
        if deve_passar_para_humano(tentativas):
            print(dados["mensagens"]["passar_para_humano"])
            print("🔔 [TRANSFERIR → Comercial]")
            break
        print(dados["mensagens"]["nao_entendi"])



