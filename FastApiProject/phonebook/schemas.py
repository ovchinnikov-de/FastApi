import re
from pydantic import BaseModel, Field


class CreateContacts(BaseModel):
    id: int
    name: str = Field(max_length=15)
    surname: str = Field(max_length=17)
    phone_number: int