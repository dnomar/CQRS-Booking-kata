Booking subject
We whant to make a booking solution for one hotel.

The first 2 users stories are :

- As a user i want to see all free rooms.
- As a user i want to book a room.
- They want to use the CQRS pattern, To do that we will have :

one command service with a function bookARoom(Booking) they call the WriteRegistry they notify the ReadRegistry called by query service with function Room[] freeRooms(arrival: Date, departure: Date)

The Booking struct contains

client id
room name
arrival date
departure date
And the Room struct contain only

room name