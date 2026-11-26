import os                                          # NOVO

from dotenv import load_dotenv                     # NOVO
from fastapi import FastAPI, Query                 # NOVO: o "Query"
from fastapi.responses import PlainTextResponse
from bot.whatsapp import extrair_mensagem    # NOVO

load_dotenv()                                      # NOVO
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")  # NOVO

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensagem": "A Lía está no ar!"}


@app.get("/webhook")                               # NOVO daqui para baixo
def verificar_webhook(
    modo: str = Query(None, alias="hub.mode"),
    token: str = Query(None, alias="hub.verify_token"),
    desafio: str = Query(None, alias="hub.challenge"),
):
    if modo == "subscribe" and VERIFY_TOKEN and token == VERIFY_TOKEN:
        return PlainTextResponse(desafio)
    return PlainTextResponse("Proibido", status_code=403)

@app.post("/webhook")
def receber_mensagem(dados: dict):
    resultado = extrair_mensagem(dados)
    if resultado is None:
        return {"status": "ignorado"}
    numero, texto = resultado
    print(f"Mensagem de {numero}: {texto}")
    return {"status": "recebido"}