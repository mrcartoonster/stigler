# -*- coding: utf-8 -*-
from sqlalchemy import Numeric
from sqlalchemy.orm import mapped_column
from typing_extensions import Annotated

int_pk = Annotated[int, mapped_column(primary_key=True)]
nm31 = Annotated[float, mapped_column(Numeric(precision=3, scale=1))]
nm51 = Annotated[float, mapped_column(Numeric(precision=5, scale=1))]
nm16 = Annotated[float, mapped_column(Numeric(precision=16, scale=4))]
nm41 = Annotated[float, mapped_column(Numeric(precision=4, scale=1))]
