from typing import List, Optional

from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

import src.crud.items as crud
from src.schemas.item import ItemInSchema, ItemOutSchema, UpdateItem

router = APIRouter()


@router.get(
    '/items',
    response_model=List[ItemOutSchema],
    responses={404: {"model": HTTPNotFoundError}}
    )
async def get_items(
    id: Optional[int] = None,
    value: Optional[str] = None,
    limit: Optional[int] = 5,
    offset: Optional[int] = 0
):
    return await crud.get_items(id, value, limit, offset)


@router.post(
    "/items",
    response_model=ItemOutSchema
)
async def create_item(item: ItemInSchema) -> ItemOutSchema:
    return await crud.create_item(item)


@router.patch(
    '/items',
    response_model=ItemOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
    )
async def update_item(item: UpdateItem) -> ItemOutSchema:
    return await crud.update_item(item)
