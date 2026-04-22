from api import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), index=True, unique=True)
    surname: Mapped[str] = mapped_column(String(32), index=False, unique=False)
    surname2: Mapped[str] = mapped_column(String(32), index=False, unique=False)
    quotes: Mapped[list['QuoteModel']] = relationship(back_populates='author', lazy='dynamic')

    def __init__(self, name, surname, surname2):
        self.name = name
        self.surname = surname
        self.surname2=surname2

    def to_dict(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "surname2": self.surname2} 