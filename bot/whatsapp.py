def extrair_mensagem(dados):
    valor = dados["entry"][0]["changes"][0]["value"]
    if "messages" not in valor:
        return None 
    mensagem = valor["messages"][0]
    numero = mensagem ["from"]
    if mensagem["type"] != "text":
        return numero, None
    return numero, mensagem["text"]["body"]