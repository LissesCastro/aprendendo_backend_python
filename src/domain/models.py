
# 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CreditCard(Base):
    """Entidade que representa um cartão de crédito."""

    __tablename__ = "credit_cards"
    id = Column(Integer, primary_key=True, autoincrement=True, Index=True)
    number = Column(String(16), nullable=False, unique=True)
    expiration_date = Column(String(5), nullable=False)  # Formato MM/AA

    def mask_number(self) -> str:
        """Retorna uma versão mascarada do número do cartão."""

        if not self.number:
            return ""
        n = self.number.strip()
        return "*" * (len(n) - 4) + n[-4:] # Para retornar algo como ******1234 
    
    def last_four_digits(self) -> str:
        """Retorna os últimos quatro dígitos do cartão."""
        
        if not self.number:
            return ""
        return self.number[-4:]