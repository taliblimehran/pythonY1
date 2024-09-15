def main():
    carbon_per_km = 7.8841
    length_flight = int(input("Enter the length of the first flight (km). End with a negative value.\n"))
    if length_flight < 0:
        print("You did not enter any flights.")
    else:
        total_distance = 0
        number_of_flights = 0
        while length_flight > 0:
            total_distance += length_flight
            number_of_flights += 1
            average_flight = total_distance / number_of_flights
            total_co2 = total_distance * carbon_per_km

            length_flight = int(input("Enter the length of the next flight (km). End with a negative value.\n"))
            if length_flight < 0:
                print(f"The length of the average flight in the last month was {average_flight} km.")
                print(f"The billionaire flew {total_distance} kilometers altogether last month and emitted {total_co2} kilograms of carbon.")


main()