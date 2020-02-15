# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is the base class for the structure

class Vehicle:
  pass

class GroundVehicle(Vehicle):
  pass
# GroundVehicle inherits from Vehicle

class Car(GroundVehicle):
  pass
# Car inherits from GroundVehicle which inherits from the base class Vehicle

class Motorcycle(GroundVehicle):
  pass
# Motorcycle inherits from GroundVehicle which inherits from the base class Vehicle

class FlightVehicle(Vehicle):
  pass
# FlightVehicle inherits from Vehicle

class Starship(FlightVehicle):
  pass
# Starship inherits from FlightVehicle which inherits from the base class Vehicle

class Airplane(FlightVehicle):
  pass
# Airplane inherits from FlightVehicle which inherits from the base class Vehicle
