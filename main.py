# -*- coding: utf-8 -*-
from fastapi import FastAPI
from graphene import Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from app.gql.queries import Query

# # from starlette_graphene3 import GraphQLApp, make_playground_handler


schema = Schema(query=Query)

app = FastAPI()


# When deploying, you'll want it to be sent to /
app.mount(
    "/",
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
