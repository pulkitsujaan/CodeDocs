class Train:
    def __init__(self,TrainName,Seats,TicketPrice):
        self.TrainName=TrainName
        self.Seats=Seats
        self.TicketPrice=TicketPrice
        self.AvailableSeats=Seats
    
    def GetTrainInfo(self):
        print(f"Train Name - {self.TrainName}\nNo. of seats - {self.Seats}\nTicket Price - {self.TicketPrice}")
    
    def BookTrain(self,NameofParticipant):
        if self.AvailableSeats<=0:
            print("Not enough Seats available.")
        else:
            print(f"Booking Confirmed in the name of {NameofParticipant}. Your seat number is {self.Seats}")
            self.AvailableSeats=self.AvailableSeats-1

intercity=Train('Rajdhani Express',100,200)
local=Train('Hawda',100,20)

local.GetTrainInfo()
local.BookTrain("Pulkit")
local.BookTrain(input("Enter your name:"))