import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from src.app.adapters.repositories import AbstractRepository
from src.app.model.booking import Booking
from datetime import date, timedelta
from src.app.adapters.repositories import FakeBookingRepository


def get_list_of_booking_of_a_room(room:str, arrival:date, departure:date, repositories:AbstractRepository):
    return [x for x in repositories.list() if x.room_name==room]

def is_between(prop_date:date, init_date:date, end_date:date):
    return True if prop_date >= init_date and prop_date<=end_date else False

def date_range_after(propose_date:date, booking_list:list):
   return [x for x in booking_list if x.departure_date>=propose_date]

def date_range_before(propose_date:date, booking_list:list):
   return [x for x in booking_list if x.arrival_date<=propose_date]

def is_room_available(room_name:str, arrival:date, departure:date, hotel_room_list:[Booking]):
    room_list=get_list_of_booking_of_a_room(room_name, arrival, departure, hotel_room_list)
    if not not room_list:
        room_list = date_range_after(arrival, room_list)
        room_list = date_range_before(departure, room_list)
        reservoir_days=get_reservoir_days(arrival, departure)
        for i in reservoir_days:
            for x in room_list:
                if is_between(i,x.arrival_date,x.departure_date):
                    return False 
    return True

def get_reservoir_days(arrival:date,departure:date):
    days=[]
    arrival_d=arrival
    if arrival_d > departure:
        raise Exception("La fecha de llegada no puede ser mayor a la de salida")
    while arrival_d != departure + timedelta(days=1):
        days.append(arrival_d)
        arrival_d = arrival_d + timedelta(days=1)
    return days

def get_all_available_rooms(arrival:date, departure:date, repo: AbstractRepository):
    available_rooms=[]
    hotel_rooms_book=repo.list()
    for x in hotel_rooms_book:
        if is_room_available(x.room_name, arrival, departure, repo):
            available_rooms.append(x.room_name)
    return available_rooms
        
