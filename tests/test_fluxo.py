from bot.fluxo import carregar_dados, decidir_escolha, decidir_comercial, classificar_texto

dados = carregar_dados("dados/exemplo.json")


def test_zero_encerra():
    assert decidir_escolha("0", dados) == ("encerrar", None)


def test_tres_vai_para_comercial():
    assert decidir_escolha("3", dados) == ("comercial", None)


def test_numero_do_menu_encaminha_para_o_setor():
    assert decidir_escolha("2", dados) == ("encaminhar", "Financeiro")


def test_texto_qualquer_nao_entende():
    assert decidir_escolha("abc", dados) == ("nao_entendi", None)


def test_comercial_salao_vai_para_consultor():
    assert decidir_comercial("1", dados) == ("encaminhar", "Consultor")


def test_comercial_consumidor_vai_para_representante():
    assert decidir_comercial("2", dados) == ("encaminhar", "Representante comercial")


def test_comercial_resposta_invalida_vai_para_humano():
    assert decidir_comercial("abc", dados) == ("passar_para_humano", "Comercial")


def test_classifica_boleto_como_financeiro():
    assert classificar_texto("Quero a segunda via do BOLETO", dados) == "2"


def test_classifica_pedido():
    assert classificar_texto("meu pedido não chegou", dados) == "1"


def test_classifica_reclamacao_como_ouvidoria():
    assert classificar_texto("quero fazer uma reclamação", dados) == "5"


def test_texto_sem_palavra_conhecida_nao_classifica():
    assert classificar_texto("oi tudo bem", dados) is None
    