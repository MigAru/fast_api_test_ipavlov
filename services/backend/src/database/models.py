from tortoise import fields, models


class Item(models.Model):
    id = fields.IntField(pk=True)
    value = fields.TextField()
    timestamp = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id} | value: {self.value}"

    class Meta:
        ordering = ["id", ]
