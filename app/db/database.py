# -*- coding: utf-8 -*-
import os

import humps
from doppler_env import load_dotenv
from sqlalchemy import URL, MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

load_dotenv()
env = dict(os.environ)

host = 'postgres://stigler_user:BJtf2dQz3GvU3iUcC99PUi0njJBoBEQ0@dpg-cnmbargl6cac73fb6pn0-a.oregon-postgres.render.com/stigler'

url_object = URL.create(
    "postgresql+psycopg2",
    username=env["DB_USER"],
    password=env["DB_PASSWORD"],
    host=env["DB_HOST"],
    database=env["DB_NAME"],
    port=int(env["PORT"]),
)


class Model(DeclarativeBase):
    """
    Base for all ORM models.
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return humps.decamelize(cls.__name__) + "s"

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )


engine = create_engine(url_object, echo=False)
Session = sessionmaker(engine)
