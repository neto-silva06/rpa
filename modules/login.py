from config.settings import *
from modules.utils import screenshot_erro
from modules.components.obter_componente import obter_componente
from modules.components.preencher_componente import preencher_campo

import time


def realizar_login(
    janela,
    usuario_valor,
    senha_valor,
    empresa_valor
):

    try:

        usuario = obter_componente(
            janela,
            "TMaskEdit",
            LOGIN_USUARIO_INDEX
        )

        senha = obter_componente(
            janela,
            "TMaskEdit",
            LOGIN_SENHA_INDEX
        )

        empresa = obter_componente(
            janela,
            "TEdit",
            LOGIN_EMPRESA_INDEX
        )

        botao_entrar = obter_componente(
            janela,
            "TBitBtn",
            LOGIN_BOTAO_ENTRAR_INDEX
        )

        preencher_campo(usuario, usuario_valor)

        preencher_campo(senha, senha_valor)

        preencher_campo(empresa, empresa_valor)

        time.sleep(1)

        botao_entrar.click_input()

        time.sleep(5)

    except Exception as e:

        screenshot_erro("erro_login")

        raise Exception(
            f"Erro ao realizar login: {e}"
        ) from e