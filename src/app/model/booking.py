from dataclasses import dataclass

@dataclass
class Booking:
    client_id:str
    room_name:str
    arrival_date:str
    departure_date:str



