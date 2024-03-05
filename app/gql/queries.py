# -*- coding: utf-8 -*-
from graphene import Field, Int, List, ObjectType
from sqlalchemy import select

from app.db.database import Session
from app.db.models import Stigler
from app.gql.types import StiglerType


class Query(ObjectType):
    foods = List(StiglerType, limit=Int())
    food = Field(StiglerType, idx=Int(required=True))

    @staticmethod
    def resolve_foods(root, info, limit=None):
        with Session() as session:
            if limit is not None:
                return session.scalars(select(Stigler).limit(limit)).all()
            else:
                return session.scalars(select(Stigler)).all()

    @staticmethod
    def resolve_food(root, info, idx):
        with Session() as session:
            return session.scalar(select(Stigler).where(Stigler.idx == idx))
