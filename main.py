from modules.openERP import abrir_erp
from modules.login import realizar_login
from modules.components.chamar_modulo_financeiro import ir_para_modulo_financeiro
from modules.components.chamar_tela_finan40155 import ir_para_contas_pagar
from modules.components.importar_arquivo import importar_arquivo
from config.settings import *
from pywinauto import Desktop
import pyautogui
import time
def executar_robo():
    app, janela = abrir_erp()

    realizar_login(
        janela=janela,
        usuario_valor=USUARIO_LOGIN,
        senha_valor=SENHA_LOGIN,
        empresa_valor=EMPRESA_LOGIN
    )

    print("Login realizado")

    time.sleep(2)

    ir_para_modulo_financeiro()

    ir_para_contas_pagar()

    importar_arquivo()