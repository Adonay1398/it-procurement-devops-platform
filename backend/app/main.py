from fastapi import FastAPI
from app.api.router import api_router

def create_app() -> FastAPI:
    app = FastAPI(
	title ="IT Procurement DevOpsPlatform",
	version = "0.1.0",
	description = "Automatización del proceso de compras TI"
     )



    app.include_router(api_router)

    return app

app = create_app()
