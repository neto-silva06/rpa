from pywinauto.application import Application

CAMINHO_ERP = r"C:\Siagri\Oracle\Bin\Login.exe"

def abrir_erp():

    app = Application(backend="win32").start(CAMINHO_ERP)

    janela = app.window(
        title_re=".*Efetuar o Login.*"
    )

    janela.wait("visible", timeout=60)

    return app, janela