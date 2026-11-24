import json

def carregar_dados(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)
