from types import TracebackType
from typing import Optional, Self, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from movies.settings import Settings


class DatabaseConnectionHandler:
    def __init__(self) -> None:
        self._connection_string = Settings().DATABASE_URL
        self._engine = create_engine(self._connection_string)
        self._session: Optional[Session] = None

    def __enter__(self) -> Self:
        self._session = sessionmaker(bind=self._engine)()
        return self

    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None:
        if self.session:
            self.session.close()

    @property
    def session(self) -> Session:
        if self._session is None:
            raise RuntimeError('Session not initialized. Use within a context manager.')
        return self._session
