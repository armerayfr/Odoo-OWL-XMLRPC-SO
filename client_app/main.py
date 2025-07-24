from fastapi import FastAPI
from interfaces.api import router

app = FastAPI(title="Odoo XML-RPC Client Service")
app.include_router(router)
