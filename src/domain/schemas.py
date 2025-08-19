from pydantic import BaseModel, Annotated, Field, constr
from typing import Optional
from pydantic import model_validator, field_validator

class CreditCardSchema(BaseModel):
    """Schema para o cartão de crédito na API.
    Usado na entrada (request body) e saída (response).
    """

    id: Optional[int] = None
    number:str = Field(min_length=16, max_length=16)
    expiration_date: str = Field(regex="^(0[1-9]|1[0-2])\/\d{2}$")

    class Config:
        """Configurações adicionais para o modelo."""
        orm_mode = True


