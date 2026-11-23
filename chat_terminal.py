import json

with open("dados/exemplo.json", encoding="utf-8") as f:
    dados = json.load(f)

print(dados["mensagens"]["saudacao"])
print(dados["mensagens"]["pedir_nome"])
nome = input("<")
print(dados["mensagens"]["apresentar_menu"].format(nome=nome))
print()
for opcao, info in dados["menu"].items():
    print(f"{opcao}. {info['nome']}")


