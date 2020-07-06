from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Event:
    @property
    def ocurred_on(self):
        return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


@dataclass
class RoomBooked(Event):
    client_id:    str
    room_name:    str
    arrival_date:date
    departure_date:date

    def to_dict(self):
        return {
            'client_id':self.client_id
            ,'room_name':self.room_name
            ,'arrival_date':self.arrival_date
            ,'departure_date':self.departure_date
            ,'ocurred_on':self.ocurred_on
        }
        

