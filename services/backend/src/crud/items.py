from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, ParamsError
from tortoise.query_utils import Q

from src.database.models import Item
from src.schemas.item import ItemOutSchema


async def get_items(id, value, limit, offset):
    try:
        if id or value:
            return await ItemOutSchema.from_queryset(
                Item.filter(Q(id=id) | Q(
                    value__icontains=value
                )).limit(limit).offset(offset)
            )
        return await ItemOutSchema.from_queryset(
            Item.all().limit(limit).offset(offset)
        )
    except ParamsError:
        raise HTTPException(
            status_code=400,
            detail="limit не может быть = 0 | offset не может быть < 0"
        )


async def create_item(item) -> ItemOutSchema:
    item_obj = await Item.create(**item.dict(exclude_unset=True))
    return await ItemOutSchema.from_tortoise_orm(item_obj)


async def update_item(item) -> ItemOutSchema:
    try:
        await ItemOutSchema.from_queryset_single(
            Item.get(id=item.id)
        )
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail=f"Item id:{item.id} не найден"
        )
    await Item.filter(id=item.id).update(value=item.value)
    return await ItemOutSchema.from_queryset_single(Item.get(id=item.id))
