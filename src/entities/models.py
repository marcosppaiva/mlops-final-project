from pydantic import BaseModel

from .enums import Condition, ResidenceType


class Imovel(BaseModel):
    district: str
    property_type: ResidenceType
    bathroom: int
    metric: float
    room: int
    energy_certify: str
    condition: Condition
