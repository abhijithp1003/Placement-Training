from datetime import datetime
class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno
    def get_ac(self):
        return self.ac
    def get_cap(self):
        return self.cap
    
    def display(self):
        print("Bus No. : {}".format(self.bno))
        print("AC : {}".format(self.ac))
        print("Capacity : {}".format(self.cap))


class Booking:
    def __init__(self):
        name = input("Enter your name: ")
        bno = int(input("Enter the bus number: "))
        d = input("Enter the date(dd-mm-yyyy): ")
        date = datetime.strptime(d, "%d-%m-%Y").date()

        self.name = name
        self.bno = bno
        self.date = date

    def isAvailable(self, BUSES, BOOKINGS, bno, date):
        booked = 0
        capacity = 0
        
        for i in BUSES:
            if i.bno == bno:
                capacity = i.cap

        for i in BOOKINGS:
            if i.bno == bno and i.date == date:
                booked += 1


        return booked < capacity

    def make_booking(self, BUSES, BOOKINGS):
        if self.isAvailable(BUSES, BOOKINGS, self.bno, self.date):
            BOOKINGS.append(self)
            print("Booking successful...")
        else:
            print("Bus is not available...")
    
    def display_booking_info(self):
        print("Name : {}".format(self.name))
        print("Bus No. : {}".format(self.bno))
        print("Date : {}".format(self.date))

    

BUSES = [Bus(1, True, 2), Bus(2, False, 50), Bus(3, True, 45)]

print("--- AVAILABLE BUSES ---")
for i in BUSES:
    i.display()
    print("-----------------------")

BOOKINGS = []

while True:
    print("--- Booking Menu ---")
    print("1. Book Bus")
    print("2. View Bookings")
    print("3. Exit")

    ch = int(input("Enter your choice: "))
    print("-----------------------")

    match ch:
        case 1:
            b = Booking()
            b.make_booking(BUSES, BOOKINGS)
        case 2:
            if not BOOKINGS:
                print("No bookings yet.")
            else:
                for i in BOOKINGS:
                    i.display_booking_info()
                    print("-----------------------")
        case 3:
            print("Thank you...")
            break

