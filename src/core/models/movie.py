from dataclasses import dataclass


@dataclass
class Movie:
    id: int
    title: str
    year: int
    duration: str
    