from sqlalchemy import Column, BigInteger, String, Integer, Numeric, DateTime, CheckConstraint
from sqlalchemy.sql.functions import current_timestamp

from app import db


class Estacoes(db.Model):

    __tablename__ = 'Estacoes'

    id_estacao = (Integer, primary_key=True)
    nome_estacao = nome = Column(String(128), nullable=False)
    cod_regiao = Column(Integer)
    uf = Column(String(2))
    codigo_wmo = Column(String(100))
    latitude = Column(Numeric(10,2))
    longitude = Column(Numeric(10,2))
    altitude = Column(Numeric(10,2))
    data_fundacao =  Column(DateTime)

    def __init__(self, id_estacao: int = 0, nome_estacao: str ="", cod_regiao: int = 0, uf: str = "", codigo_wmo: str = "",
                 latitude: float = 0.0, longitude:float = 0.0,) -> None:
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


    def
