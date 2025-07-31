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
        bno = int(input("Enter bus number: "))
        d = input("Enter date: ")
        date = datetime.strptime(d, "%d-%m-%Y").date()

        self.bno = bno
        self.name = name
        self.date = date

    def make_booking(self, BUSES, BOOKINGS):
        if isAvailable(BUSES, BOOKINGS,self.bno, self.date):
            BOOKINGS.append(self)
        else:
            print("Bus is not available.")
    
    def is
            

BUSES = [Bus(1, True, 2), Bus(2, False, 50), Bus(3, True, 45)]
print("--- AVAILABLE BUSES ---")
for i in BUSES:
    i.display()
    print("-----------------------")

BOOKINGS = []

while True:
    print("--- BOOKING MENU ---")
    print("1. Book Bus")
    print("2. View Bookings")
    print("3. Exit")
    
    choice = input("Enter choice: ")

    match choice:
        case '1':
            b = Booking()
            b.make_booking(BUSES, BOOKINGS)
        case '2':
            if not BOOKINGS:
                print("No bookings yet.")
                continue
            else:
                b.view_bookings(BOOKINGS)
        case '3':
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid choice.")