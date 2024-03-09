# -*- coding: utf-8 -*-
from graphene import Field, Int, List, ObjectType
from graphql import GraphQLError
from sqlalchemy import select

from app.db.database import Session
from app.db.models import Stigler
from app.gql.types import StiglerType


class Query(ObjectType):
    foods = List(StiglerType, limit=Int(), skip=Int())
    food = Field(StiglerType, idx=Int(required=True))

    @staticmethod
    def resolve_foods(root, info, limit=None, skip=None):
        with Session() as session:
            if limit is None and skip is not None:
                return GraphQLError("Limit must be specified with skip.")

            if limit:
                return session.scalars(
                    select(Stigler).limit(limit).offset(skip),
                ).all()

            else:
                return session.scalars(select(Stigler)).all()

    @staticmethod
    def resolve_food(root, info, id):
        with Session() as session:
            return session.scalar(select(Stigler).where(Stigler.idx == id))
