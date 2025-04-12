from tortoise.models import Model
from tortoise import fields


class TaskDB(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    is_completed = fields.BooleanField(default=False)
