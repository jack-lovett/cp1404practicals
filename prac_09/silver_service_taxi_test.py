from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Limo", 100, 2)
fancy_taxi.drive(18)
print(fancy_taxi)
print(f"Fare: ${fancy_taxi.get_fare()}")
