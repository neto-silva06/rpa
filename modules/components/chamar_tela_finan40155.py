from pywinauto import Desktop
import pyautogui
def ir_para_contas_pagar():       
        
        opcoes = Desktop(backend="win32").window(
        class_name="TFOpcoes"
        )

        campo = opcoes.child_window(
        class_name="TEdit",
        found_index=1
        )

        campo.set_focus()
        

        campo.type_keys("Finan40155", with_spaces=True)

        botao_ir = opcoes.child_window(
        title="&Ir",
        class_name="TBitBtn"
        )

        botao_ir.click()
        botao_ir.click()