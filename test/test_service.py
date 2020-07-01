import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
import datetime
from src.app.adapters.repositories import FakeBookingRepository
from src.app.model.booking import Booking
from src.app.service_layer.service import available_rooms


today=datetime.date.today()
today_plus_2=datetime.timedelta(days=2)
today_plus_10=datetime.timedelta(days=10)

def test_get_available_rooms():
    hotel=FakeBookingRepository()
    for i in range(10):
        hotel.add(Booking(
            client_id="",
            room_name=f"room-{i}",
            arrival_date="",
            departure_date=""
        ))
    av_rooms=available_rooms(hotel)
    assert len(av_rooms)==10 


