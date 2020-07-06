from src.app.model.booking import Booking
from src.app.model.events import Event, RoomBooked
import abc
import json

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def list():
        raise NotImplemented


class FakeBookingRepository(AbstractRepository):

    def __init__(self):
        self.commit=False
        self._booking=[]

    def add(self, booking:Booking):
        self._booking.append(booking)
        FakeEventStoreRepository.add(RoomBooked(booking.client_id,booking.room_name,booking.arrival_date,booking.departure_date))
    
    def list(self)->[]:
        return self._booking

    def get_room(self, name:str)->Booking:
        for room in self._booking:
            if room.room_name == name:
                return room


class FakeEventStoreRepository():
    _events=[]

    @staticmethod
    def add(event:Event):
      FakeEventStoreRepository._events.append(event.to_dict())

    @staticmethod
    def list_from(event_id:int)->[]:
        return [x for x in FakeEventStoreRepository._events if x.index(x) >= event_id]
    
    @staticmethod
    def clear():
        FakeEventStoreRepository._events=[]

    @staticmethod
    def list_all():
        return FakeEventStoreRepository._events


