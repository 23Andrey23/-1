from dataclasses import dataclass


@dataclass
class Person:
    name: str = None
    surname: str = None
    email: str = None
    phone: str = None
