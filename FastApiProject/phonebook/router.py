from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from phonebook.models import users
from database import get_async_session
from phonebook.schemas import CreateContacts

router = APIRouter(tags=['Phonebook'])


@router.post('/contacts/add')
async def add_contacts(new_contacts: CreateContacts, session: AsyncSession = Depends(get_async_session)):
    statement = insert(users).values(**new_contacts.dict())
    await session.execute(statement)
    await session.commit()
    return {'status':'ok'}


@router.get('/contacts')
async def all_contacts(session: AsyncSession = Depends(get_async_session)):
    query = select(users)
    result = await session.execute(query)
    return result.mappings().all()

@router.get('/contacts/search')
async def search_contacts(name: str,session: AsyncSession = Depends(get_async_session)):
    query = select(users).where(users.c.name==name)
    result = await session.execute(query)
    return result.mappings().all()


