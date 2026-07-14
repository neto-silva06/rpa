import time
from modules.utils import screenshot_erro


def preencher_campo(
    campo,
    valor,
    limpar=True
):
    """
    Preenche um campo de forma robusta.
    """

    try:

        campo.wait(
            "exists enabled visible ready",
            timeout=10
        )

        campo.set_focus()

        time.sleep(0.3)

        if limpar:

            campo.type_keys(
                "^a{BACKSPACE}",
                pause=0.05
            )

            time.sleep(0.2)

        campo.type_keys(
            str(valor),
            with_spaces=True,
            pause=0.05
        )

    except Exception as e:

        screenshot_erro("erro_preencher_campo")

        raise Exception(
            f"Erro ao preencher campo "
            f"com valor [{valor}]: {e}"
        ) from e