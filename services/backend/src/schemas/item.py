from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Item

ItemInSchema = pydantic_model_creator(
    Item, name="ItemIn", exclude_readonly=True)
ItemOutSchema = pydantic_model_creator(
    Item, name="Item"
)


class UpdateItem(BaseModel):
    id: Optional[int]
    value: Optional[str]
