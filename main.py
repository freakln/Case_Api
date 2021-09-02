import uvicorn
from fastapi import FastAPI

from controllers.api_controller import api_initializer
from controllers.currency_controller import convert_from_to
# inicializa as moedas no sistema
Currency = api_initializer()

# inicializa a api
app = FastAPI()


@app.get("/convert/")
def convert(frm: str = 'USD', to: str = 'USD', amount: float = 1.0):
    return convert_from_to(frm, to, amount, Currency)


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080)
