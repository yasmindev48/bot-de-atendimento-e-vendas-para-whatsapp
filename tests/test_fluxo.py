from bot.fluxo import carregar_dados, decidir_escolha

dados = carregar_dados("dados/exemplo.json")


def test_zero_encerra():
    assert decidir_escolha("0", dados) == ("encerrar", None)


def test_tres_vai_para_comercial():
    assert decidir_escolha("3", dados) == ("comercial", None)


def test_numero_do_menu_encaminha_para_o_setor():
    assert decidir_escolha("2", dados) == ("encaminhar", "Financeiro")


def test_texto_qualquer_nao_entende():
    assert decidir_escolha("abc", dados) == ("nao_entendi", None)
    