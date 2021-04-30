class OneWayFlightBooking:

    def __int__(self, from_location, to_location, departure_date, travellers, travel_class):
        print("init executed and self is:", self)
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travellers = travellers
        self.travel_class = travel_class

    def show_details(self):
        print("travel detail from {} to {} on {} for {} travellers in {} class".format(self.from_location, self.to_location,
                                                                       self.departure_date, self.travellers, self.travel_class))


def main():

    oref1 = OneWayFlightBooking("Delhi", "Bangalore", "6th August, 2021", 2, "economy")
    oref1.departure_date = "6th August, 2021"
    print("oref1 is:", oref1)
    print("oref1 is:", oref1.__dict__)

    print()

    oref2 = OneWayFlightBooking("goa", "ludhiana", "10th August, 2021", 2, "buisness")
    oref2.travellers = 5
    oref2.travel_class = "buisness"
    print("oref2 is:", oref2)
    print("oref2 object's data is:", oref2.__dict__)

    print()

    oref1.show_details()
    oref2.show_details()

print("class detail's", OneWayFlightBooking.__dict__)
if __name__ == '__main__':
    main()