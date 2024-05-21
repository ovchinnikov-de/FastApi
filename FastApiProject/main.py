from fastapi import FastAPI
from phonebook.router import router
from fastapi.staticfiles import StaticFiles
from render.render import router as router_contacts
app = FastAPI(title="Список контактов")


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
app.include_router(router_contacts)

