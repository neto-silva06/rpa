from fastapi import FastAPI,Header
from threading import Thread
from main import executar_robo

app = FastAPI()


@app.get("/executar")
def executar():
    
    def processo():
        executar_robo()

    Thread(target=processo).start()

    return {
        "status": "executando"
    }