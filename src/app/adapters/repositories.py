from src.app.model.booking import Booking
import abc

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
    
    def list(self)->[]:
        return self._booking

    def get_room(self, name:str)->Booking:
        for room in self._booking:
            if room.room_name == name:
                return room


