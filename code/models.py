from tortoise import fields, Model


class Review(Model):
    id = fields.IntField(pk=True)
    text = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'reviews'
