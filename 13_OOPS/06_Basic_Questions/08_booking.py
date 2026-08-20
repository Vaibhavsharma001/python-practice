# Write a class Train which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class Train:
    def __init__(self,ticket,seats,fare,fro,to,train_number):
        self.ticket = ticket
        self.seats = seats
        self.fare = fare
        self.fro = fro
        self.to = to
        self.train_number= train_number
        
    def book_tickets(self):
        if self.ticket>0 and self.ticket <= self.seats:
            self.seats = self.seats - self.ticket
            print(f"thanks for booking. You have booked {self.ticket} tickets from {self.fro} to {self.to} in train number {self.train_number}")
            
        elif self.ticket>self.seats:
            print("failed no more seats")
            
        else:
            print("failed minimum one ticket you have to book")
    
    def available_seats(self):
        return self.seats
    
    def fare_information(self):
         print(f"Ticket fare is ₹{self.fare}")
        

booking = Train(
    ticket = int(input("enter no of tickets---")),
    seats = 100,
    fare = 40,
    fro = "Delhi",
    to = "Agra",
    train_number = 63345
)

booking.book_tickets()
print(f"remaining seats: {booking.available_seats()}")
booking.fare_information()