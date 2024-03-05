# -*- coding: utf-8 -*-
from graphene import List, ObjectType
from sqlalchemy import select

from app.db.database import Session
from app.db.models import Stigler
from app.gql.types import StiglerType


class Query(ObjectType):
    users = List(StiglerType)

    @staticmethod
    def resolve_users(root, info):
        with Session() as session:
            return session.scalars(select(Stigler)).all()
