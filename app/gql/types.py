# -*- coding: utf-8 -*-
from graphene import Float, Int, ObjectType, String


class StiglerType(ObjectType):
    class Meta:
        description = "Stigler type!"
        name = "Stigler"

    idx = Int()
    commodity = String()
    unit = String()
    price_cents = Float()
    calories = Float()
    protein_g = Float()
    calcium_g = Float()
    iron_mg = Float()
    vitamin_a_iu = Float()
    vitamin_b1_iu = Float()
    vitamin_b2_iu = Float()
    niacin_mg = Float()
    vitamin_c_mg = Float()
