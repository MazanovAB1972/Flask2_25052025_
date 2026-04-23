from api import ma
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema
from marshmallow import EXCLUDE

def rating_validate(value: int):
    return value in (1,6)

class QuoteSchema(ma.SQLAlchemySchema):
      class Meta:
        model = QuoteModel
        dump_only = ("id",)

      unknown = EXCLUDE
      text = ma.auto_field()
      author = ma.Nested(AuthorSchema(only=("name","surname")))
      rating = ma.auto_field(strict=True, validate=rating_validate)                           

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)       