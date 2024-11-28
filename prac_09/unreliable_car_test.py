"""CP1404 Practical 9"""

from prac_09.unreliable_car import UnreliableCar

bad_car = UnreliableCar("Prius 1", 100, 40)
bad_car.drive(40)
print(bad_car)
bad_car.drive(100)
print(bad_car)
