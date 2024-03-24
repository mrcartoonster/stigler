# -*- coding: utf-8 -*-
from fastapi import FastAPI
from graphene import Schema
from sqlalchemy import select
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from app.db.database import Session
from app.db.models import Stigler
from app.gql.queries import Query

# # from starlette_graphene3 import GraphQLApp, make_playground_handler


schema = Schema(query=Query)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world"}


@app.get("/foods/")
def foods():
    with Session() as session:
        results = session.execute(select(Stigler)).scalars()
        return results


# When deploying, you'll want it to be sent to /
app.mount(
    "/graphql",
    GraphQLApp(
        schema=schema,
        on_get=make_graphiql_handler(),
    ),
)

# This is for localhost testing
# app.mount(
#     "/graphql",
#     GraphQLApp(
#         schema=schema,
#         on_get=make_graphiql_handler(),
#     ),
# )
