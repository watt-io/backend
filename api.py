import redis
import uuid
from typing import List
from dataclasses import dataclass

redis = redis.StrictRedis('localhost', decode_responses=True)

genid = lambda: str(uuid.uuid4()).replace('-','')

@dataclass
class Movies:
    nome: str = None
    movie_id: str = genid()
    # usaremos redis para persistir os dados em memória
    # já que é uma pequena quantidade de dados
    # caso fosse escalar, um ORM seria mais performático

    def insert_movie(self) -> bool:
        '''
        não há necessidade de checar duplicidade de números
        gerados pelo uuid uma vez que a probabilidade de
        acontecer isso é infíma
        '''
        try:
            redis.set(f"{self.movie_id}", self.nome)
            return True
        except Exception as E:
            return (False, E)

    @classmethod
    def list_all(cls) -> List[str]:
        try:
            temp_key = genid()
            ids = [key for key in redis.keys() if len(key) == len(temp_key)]
            if ids:
                nomes = redis.mget(ids)
                return nomes
            else:
                return False
        except Exception as E:
            return E

    def unique_movie(self) -> List[str]:
        try:
            resp = redis.get(self.movie_id)
            return False if not resp else resp
        except Exception as E:
            return E