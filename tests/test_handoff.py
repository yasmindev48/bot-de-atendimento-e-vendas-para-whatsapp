from bot.handoff import deve_passar_para_humano


def test_nao_passa_com_zero_tentativas():
    assert deve_passar_para_humano(0) is False


def test_nao_passa_com_uma_tentativa():
    assert deve_passar_para_humano(1) is False


def test_passa_com_duas_tentativas():
    assert deve_passar_para_humano(2) is True