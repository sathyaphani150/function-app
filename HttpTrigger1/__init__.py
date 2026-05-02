import azure.functions as func
from config import Config

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'User')

    return func.HttpResponse(
        f"Hello {name}, API_KEY={Config.API_KEY}, ENV={Config.ENV}"
    )