import sys
sys.path.append(r"C:\Users\van-gerald.olivares\Documents\08 Code\CQRS-kata")
from datetime import date, timedelta
from src.app.adapters.repositories import FakeBookingRepository
from src.app.model.booking import Booking
from src.app.service_layer.service import is_between, date_range_after,date_range_before, is_room_available

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

def test_get_if_space_is_available():
   
    desired_booking=(Booking(
        client_id="cliente-01",
        room_name="room-1",
        arrival_date=date(2020,7,22),
        departure_date=date(2020,7,24)
    ))

    booked_rooms=FakeBookingRepository()
    """ booked_rooms.add(Booking(
        client_id="",
        room_name=f"room-1",
        arrival_date=date(2020, 6, 25),
        departure_date=date(2020, 6, 30)
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
    )) """  
    
    assert is_room_available(desired_booking, booked_rooms.list())


