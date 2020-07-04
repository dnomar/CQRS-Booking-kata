from dataclasses import dataclass
from datetime import date

@dataclass
class Booking:
    client_id:str
    room_name:str
    arrival_date:date
    departure_date:date



