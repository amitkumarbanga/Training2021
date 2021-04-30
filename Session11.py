"""input_str = "my name is amit kumar"
output_str = input_str.upper()
print("The lowercased characters are:", output_str)"""

one_way_flight_booking = {
    "from_location": "Delhi",
    "to_location": "Bangalore",
    "departure_date": "6th Agust, 2021",
    "travellers": 2,
    "travel_class": "economy"
}

print(one_way_flight_booking, type(one_way_flight_booking))
class OnewayFlightBooking:
    pass
def main():
    oref1 = OnewayFlightBooking()
    oref2 = OnewayFlightBooking()
    oref3 = oref1


    print("OnewayFlightBooking is:", oref1, type(oref1))
    print("oref1 Object Contains:", oref1.__dict__)

    print()


    print("oref2 is:", oref2, type(oref2))
    print("oref2 Object Contains:", oref1.__dict__)

    print()

    print("oref3 is:", oref3, type(oref3))
    print("oref3 Object Contains:", oref1.__dict__)

    print()

    oref1.from_location = "Delhi"
    oref3.to_location = "Bangalore"
    oref1.departure_date = "6th August, 2021"
    oref3.travellers = 2
    oref1.travel_class = "economy"

# update operation
    oref3.departure_date = "5th August, 2022"

    oref2.from_location = "goa"
    oref2.to_location = "ludhiana"
    oref2.departure_date = "10th August, 2021"
    oref2.travellers = 2
    oref2.travel_class = "business"

    oref2.kids = 1
    oref2.kids_age = 2

    print("oref1 Object Contains:", oref1.__dict__)
    print("oref2 Object Contains:", oref2.__dict__)
    print("oref3 Object Contains:", oref3.__dict__)

# delete operation
    del oref1.travel_class
    del oref2.kids_age
    print()
    print("oref1 Object Contains:", oref1.__dict__)
    print("oref2 Object Contains:", oref2.__dict__)
    print("oref3 Object Contains:", oref3.__dict__)
    print()
# Decorated
    print("travel detail from {} to {} on {} for {} passengers".format(oref1.from_location, oref3.to_location, oref1.departure_date, oref3.travellers))
    print("travel detail from {} to {} on {} for {} passengers".format(oref2.from_location, oref2.to_location,
                                                                       oref2.departure_date, oref2.travellers))


if __name__ == '__main__':
    main()
