from src.app.adapters.repositories import AbstractRepository

def available_rooms(repository:AbstractRepository):
    available_rooms=[]
    hotel=repository.list()
    for booked_room in hotel:
        if not booked_room.client_id and not booked_room.arrival_date and not booked_room.departure_date :
            available_rooms.append(booked_room.room_name)
    return available_rooms
    

