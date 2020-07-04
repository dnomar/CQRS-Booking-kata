import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from src.app.adapters.repositories import AbstractRepository
from src.app.model.booking import Booking
from datetime import date, timedelta
from src.app.adapters.repositories import FakeBookingRepository



def get_list_of_booking_of_a_room(room:str, arrival:date, departure:date, repositories:AbstractRepository):
    return [x for x in repositories if x.room_name==room]

def is_between(prop_date:date, init_date:date, end_date:date):
    return True if prop_date >= init_date and prop_date<=end_date else False

def date_range_after(propose_date:date, booking_list:list):
   return [x for x in booking_list if x.departure_date>=propose_date]

def date_range_before(propose_date:date, booking_list:list):
   return [x for x in booking_list if x.arrival_date<=propose_date]

def is_room_available(booking:Booking, hotel_room_list:[Booking]):
    room_list=get_list_of_booking_of_a_room(booking.room_name, booking.arrival_date, booking.departure_date,hotel_room_list)
    if not not room_list:
        pass
    return False #se debe cambiar a true para que pase el test
