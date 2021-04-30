class OneWayFlightBooking:
    def __init__(self):
        print("init executed and self is:", self)
        self.from_location = "Delhi"
        self.to_location = "Bangalore"
        self.departure_date = "6th August, 2021"
        self.travellers = 2
        self.travel_class = "economy"

def main():
    oref1 = OneWayFlightBooking()
    print("oref1 is:", oref1)
    print("oref1 is:", oref1.__dict__)

    print()

    oref2 = OneWayFlightBooking()
    oref2.travellers = 5
    print("oref2 is:", oref2)
    print("oref2 is:", oref2.__dict__)


if __name__ == '__main__':
    main()