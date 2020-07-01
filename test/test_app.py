import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from src.app import app
from src.app.service_layer.service import available_rooms
from src.app.adapters.repositories import FakeBookingRepository
from src.app.model.booking import Booking
import datetime

today=datetime.date.today()
today_plus_2=datetime.timedelta(days=2)
today_plus_10=datetime.timedelta(days=10)

def test_booking_a_room_succesfully():
    """ #given
    room_name="room-1"
    booking_repo=FakeRoomsRepository()
    booking_repo.add(Booking(
        client_id="id-123",
        room_name=room_name,
        arrival_date=today_plus_2,
        departure_date=today_plus_10
    ))

    assert available_rooms(booking_repo).get["room-1"].get_name()== room_name """
    assert False
