import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from datetime import date, timedelta
from src.app.adapters.repositories import FakeBookingRepository
from src.app.model.booking import Booking
from src.app.service_layer.service import is_between, date_range_after,date_range_before, is_room_available, get_reservoir_days, get_all_available_rooms
import pytest

today=date.today()
today_plus_2=today+timedelta(days=2)
today_plus_10=today_plus_2+timedelta(days=8)

def test_return_the_booking_list_of_a_single_room():
    booked_rooms=FakeBookingRepository()
    room="room-1"
    booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date="",
        departure_date=""
    ))
    booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date=date(2020, 7, 4),
        departure_date=date(2020, 7, 12)
    ))
    booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date=date(2020, 7, 15),
        departure_date=date(2020, 7, 17)
    ))  
    booked_room_list=[x for x in booked_rooms.list() if x.room_name==room]
    booking_dataset=[ 
        Booking(client_id='', room_name='room-1', arrival_date='', departure_date=''), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 4), departure_date=date(2020, 7, 12)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 17))
        ]
    assert booked_room_list == booking_dataset

def test_return_empty_list_if_the_room_is_not_in_the_booking_list():
    booked_rooms=FakeBookingRepository()
    room="room-2"
    booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date="",
        departure_date=""
    ))
    booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date=date(2020, 7, 4),
        departure_date=date(2020, 7, 12)
    ))
    booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date=date(2020, 7, 15),
        departure_date=date(2020, 7, 17)
    ))  
    booked_room_list=[x for x in booked_rooms.list() if x.room_name==room]
    #print(booked_room_list)
    booking_dataset=[ Booking(client_id='', room_name='room-1', arrival_date='', departure_date=''), Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 4), departure_date=date(2020, 7, 12)), Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 17))]
    assert not booked_room_list

def test_if_date_is_between_a_range_of_dates():
    proposed_date_prev_range=date(2020, 7, 3)
    proposed_date_init_range=date(2020, 8, 3)
    proposed_date_whitin_range=date(2020, 8, 10)
    proposed_date_end_range=date(2020, 8, 13)
    proposed_date_after_range=date(2020, 8, 15)
    arrival_booked=date(2020, 8, 3)
    departure_booked=date(2020, 8, 13)
    assert is_between(proposed_date_prev_range, arrival_booked,departure_booked)==False
    assert is_between(proposed_date_init_range, arrival_booked,departure_booked)==True
    assert is_between(proposed_date_whitin_range, arrival_booked,departure_booked)==True
    assert is_between(proposed_date_end_range, arrival_booked,departure_booked)==True
    assert is_between(proposed_date_after_range, arrival_booked,departure_booked)==False

def test_get_the_ranges_after_the_arrival_date():
    
    proposed_arrival_1=date(2020, 7, 29)

    rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))   
    ]

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))   
    ]

    assert date_range_after(proposed_arrival_1, rooms_booking_list) == []

    proposed_arrival_1=date(2020, 7, 26)
    test_rooms_booking_list =[Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))]    
    assert date_range_after(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 23)
    test_rooms_booking_list =[Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))]    
    assert date_range_after(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 17)
    test_rooms_booking_list =[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),        
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))
        ]    
    assert date_range_after(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 13)
    test_rooms_booking_list =[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),        
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))
        ]    
    assert date_range_after(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 8)
    test_rooms_booking_list =[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),        
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))
        ]    
    assert date_range_after(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 5)
    test_rooms_booking_list =[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),        
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))
        ]    
    assert date_range_after(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

def test_get_the_ranges_before_the_departure_date():
    proposed_arrival_1=date(2020, 7, 29)

    rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))   
    ]

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))   
    ]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 26)

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20)),
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 25), departure_date=date(2020, 7, 28))   
    ]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 23)

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20))   
    ]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 17)

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8)), 
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 20))   
    ]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 13)

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8))   
    ]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 7)

    test_rooms_booking_list=[
        Booking(client_id='', room_name='room-1', arrival_date=date(2020, 7, 5), departure_date=date(2020, 7, 8))   
    ]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

    proposed_arrival_1=date(2020, 7, 3)

    test_rooms_booking_list=[]

    assert date_range_before(proposed_arrival_1, rooms_booking_list) == test_rooms_booking_list

def test_get_list_of_reservoir_days():
    
    d1=date.today()
    d2=d1 + timedelta(days=5)
    d_list=get_reservoir_days(d1,d2)
    sol_dataset=[
        date(2020,7,4),
        date(2020,7,5),
        date(2020,7,6),
        date(2020,7,7),
        date(2020,7,8),
        date(2020,7,9),
    ]
    assert d_list == sol_dataset
    
    with pytest.raises(Exception):
        d_list=get_reservoir_days(d2,d1)

def test_get_if_room_is_available():
      
    booked_rooms=FakeBookingRepository()
    assert is_room_available("room-1", date(2020,6,22), date(2020,6,24), booked_rooms)

    booked_rooms.add(Booking(client_id="", room_name="room-1", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30)))
    booked_rooms.add(Booking(client_id="", room_name=f"room-1", arrival_date=date(2020, 7, 4), departure_date=date(2020, 7, 12)))
    booked_rooms.add(Booking( client_id="", room_name=f"room-1", arrival_date=date(2020, 7, 15), departure_date=date(2020, 7, 17))) 
    
    desired_booking=(Booking( client_id="cliente-01", room_name="room-1", arrival_date=date(2020,6,22), departure_date=date(2020,6,27)))
    
    assert is_room_available("room-1", date(2020,6,22), date(2020,6,27), booked_rooms) == False

    assert is_room_available("room-1", date(2020,6,24), date(2020,6,29), booked_rooms) == False

    assert is_room_available("room-1", date(2020, 6, 28), date(2020, 7, 2), booked_rooms) == False

    assert is_room_available("room-1", date(2020, 7, 1), date(2020, 7, 3), booked_rooms)
    
    assert is_room_available("room-1", date(2020, 7, 3), date(2020, 7, 14), booked_rooms) == False

def test_get_all_free_rooms(): 
    
    arrival_date=date(2020, 6, 26)
    departure_date=date(2020, 6, 28)
    booked_rooms=FakeBookingRepository()

    #Given initial Hotel Dataset
    booked_rooms.add(Booking(client_id="client-1", room_name="room-1", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-2", room_name="room-2", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-3", room_name="room-3", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-4", room_name="room-4", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-5", room_name="room-5", arrival_date=date(2020, 6, 5), departure_date=date(2020, 6, 13))) 
    booked_rooms.add(Booking(client_id="client-6", room_name="room-6", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-7", room_name="room-7", arrival_date=date(2020, 6, 5), departure_date=date(2020, 6, 13))) 
    booked_rooms.add(Booking(client_id="client-8", room_name="room-8", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-9", room_name="room-9", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30))) 
    booked_rooms.add(Booking(client_id="client-10", room_name="room-10", arrival_date=date(2020, 6, 25), departure_date=date(2020, 6, 30)))

    available_rooms_list=get_all_available_rooms(arrival_date, departure_date, booked_rooms)

    solution_dataset=[
        "room-5",
        "room-7"
    ]
    assert available_rooms_list==solution_dataset