from abc import ABC, abstractmethod
from core.models.movie import Movie
from typing import List, Optional

class MovieInterface(ABC):
    @abstractmethod
    def add(self, movie: Movie) -> None:
        pass
    
    @abstractmethod
    def list(self) -> List[Movie]: 
        pass
                
    @abstractmethod
    def get_by_id(self, movie_id: str) -> Optional[Movie]:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Movie]:
        pass
    
    @abstractmethod
    def delete_by_title(self, title: str) -> None:
        pass

    @abstractmethod
    def update(self, movie: Movie) -> Optional[Movie]:
        pass