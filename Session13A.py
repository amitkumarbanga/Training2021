class ONEWayFlightBooking:

    def __init__(self, from_location, to_location, departure_date, travllers, travel_class):
        print("ONEWayFlightBooking Object Constructor Executed")
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.travllers = travllers
        self.travel_class = travel_class

    def show(self):
        print("Travel Details: From {} To {} On {} for {} traveller in {} class".format(self.from_location, self.to_location, self.departure_date, self.travller, self.travel_class))

class ReturnFlightBooking:

        def __init__(self, from_location, to_location, departure_date, return_date, travllers, travel_class):
            print("ReturnFlightBooking Constructor Executed")

            self.from_location = from_location
            self.to_location = to_location
            self.departure_date = departure_date
            self.travllers = travllers
            self.travel_class = travel_class
            self.return_date = return_date

        def show(self):
            print("Travel Details: From {} To {} On {} For {} travller in {} class".format(self.from_location,
                                                                                          self.to_location,
                                                                                          self.departure_date,
                                                                                          self.travllers,
                                                                                          self.travel_class))
            print("Return Date:", self.return_date)

def main():
        oRef = ONEWayFlightBooking("Delhi", "Banglore", "10th August, 2020", 4, "economy")
        oRef.show_details()
print()
        rRef = ReturnFlightBooking("Delhi", "Goa", "12th August, 2020", "20th August, 2021", 4, "economy")
        rRef.show_details()

if __name__ == '__main__':
    main()