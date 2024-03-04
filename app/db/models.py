# -*- coding: utf-8 -*-
from dataclasses import dataclass

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.annotations import int_pk, nm16, nm31, nm41, nm51
from app.db.database import Model


@dataclass
class Stigler(Model):
    """
    Stigler Model.
    """

    idx: Mapped[int_pk]
    commodity: Mapped[str] = mapped_column(String(32))
    unit: Mapped[str] = mapped_column(String(12))
    price_cents: Mapped[nm31]
    calories: Mapped[nm51]
    protein_g: Mapped[nm51]
    calcium_g: Mapped[nm16]
    iron_mg: Mapped[nm41]
    vitamin_a_iu: Mapped[nm41]
    vitamin_b1_mg: Mapped[nm31]
    vitamin_b2_mg: Mapped[nm31]
    niacin_mg: Mapped[nm41]
    vitamin_c_mg: Mapped[nm51]
