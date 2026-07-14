from pywinauto import Desktop
from modules.utils import screenshot_erro
import time
def importar_arquivo():
    try:
        janela = Desktop(backend="win32").window(
            class_name="TFFinan40155"
        )

        # plano de contas
        campo_plano = janela.child_window(
            class_name="TJvValidateEdit",
            found_index=0
        )

        campo_plano.set_focus()
        #campo_plano.type_keys("^a{BACKSPACE}")
        campo_plano.type_keys("1")

        # arquivo txt
        campo_arquivo = janela.child_window(
            class_name="TJvFilenameEdit"
        )

        campo_arquivo.set_focus()
        #campo_arquivo.type_keys("^a{BACKSPACE}")
        campo_arquivo.type_keys(
            r"C:\Users\mario.neto\Desktop\Arquivos importação\FIN_01.05.2026.txt",
            with_spaces=True
        )

        # importar
        botao_importar = janela.child_window(
            title="&Importar",
            class_name="TBitBtn"
        )

        botao_importar.click()

        time.sleep(2)

        # verifica popup de erro
        erro = Desktop(backend="win32").window(
            title_re=".*Access violation.*"
        )

        if erro.exists(timeout=2):

            
            screenshot_erro("erro_ao_importar_arquivo")

            print("ERRO IDENTIFICADO")
            


    except Exception as e:


        screenshot_erro("erro_ao_importar_arquivo")
