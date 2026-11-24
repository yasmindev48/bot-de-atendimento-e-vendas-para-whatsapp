import json

def carregar_dados(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)

    
def decidir_escolha(escolha, dados):
    if escolha == "0":
        return "encerrar", None
    if escolha == "3":
        return "comercial", None
    if escolha in dados["menu"]:
        setor = dados["menu"][escolha]["setor"]
        return "encaminhar", setor
    return "nao_entendi", None
