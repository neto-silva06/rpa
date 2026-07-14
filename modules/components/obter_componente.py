from modules.utils import screenshot_erro


def obter_componente(
    janela,
    class_name,
    found_index,
    timeout=10
):
    """
    Localiza e valida um componente da tela.
    """

    try:

        componente = janela.child_window(
            class_name=class_name,
            found_index=found_index
        )

        componente.wait(
            "exists enabled visible ready",
            timeout=timeout
        )

        return componente

    except Exception as e:

        screenshot_erro("erro_obter_componente")

        raise Exception(
            f"Erro ao localizar componente "
            f"[class_name={class_name}] "
            f"[found_index={found_index}] "
            f": {e}"
        ) from e