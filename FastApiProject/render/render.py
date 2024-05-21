from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from phonebook.router import all_contacts,search_contacts,add_contacts

router = APIRouter(
    tags=["Страницы в интернете"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/phonebook")
def get_contacts(request: Request, contacts = Depends(all_contacts)):
    return templates.TemplateResponse("get_contacts.html", {"request": request, 'contacts':contacts})


@router.get("/phonebook/search/{name}")
def get_search_page(request: Request, search=Depends(search_contacts)):
    return templates.TemplateResponse("search.html", {"request": request, "search": search})

@router.get("/phonebook/add")
def get_add(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})


@router.post("/phonebook/add")
def get_add_contact(request: Request,add =Depends(add_contacts)):
    return templates.TemplateResponse("add.html", {"request": request,"add": add})
