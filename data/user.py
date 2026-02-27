import dataclasses
import datetime
from enum import Enum

class Hobbies(Enum):
    Sports = 1
    Reading = 2
    Music = 3

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: Hobbies
    picture: str
    address: str
    state: str
    city: str

