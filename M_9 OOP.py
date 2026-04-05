import random



# Car class
class Car:
        def __init__(self, registration_number, maximum_speed):
            self.registration_number = registration_number
            self.maximum_speed = maximum_speed
            self.current_speed = 0
            self.travelled_distance = 0

        def accelerate(self, change_in_speed):
            self.current_speed += change_in_speed

            if self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            if self.current_speed < 0:
                self.current_speed = 0

        def drive(self, hours):
            distance_covered = self.current_speed * hours
            self.travelled_distance += distance_covered

# Electric Car
class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


# Gasoline Car
class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

# Race class
class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n {self.name} Status")
        print(f"{'Reg No':<10}  {'Max Speed':<12}  {'Speed':<12}  {'Distance'}")
        print("-" * 55)

        for car in self.cars:
            print(f"{car.registration_number:<10}  {car.maximum_speed:<9} km/h  "
                  f"{car.current_speed:<9} km/h  {int(car.travelled_distance):<6} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False

# Main
new_car = Car("ABC-123", 142)
print(f"Reg: {new_car.registration_number}, Max Speed: {new_car.maximum_speed}, "
      f"Current Speed: {new_car.current_speed}, Distance: {new_car.travelled_distance}")

# Create Electric Car
electric_car = ElectricCar("ABC-15", 180, 52.5)

# Create Gasoline Car
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Set speeds
electric_car.accelerate(120)
gasoline_car.accelerate(100)

# Drive for 3 hours
electric_car.drive(3)
gasoline_car.drive(3)

# Print results
print("\nElectric Car Distance:", electric_car.travelled_distance, "km")
print("Gasoline Car Distance:", gasoline_car.travelled_distance, "km")

# Acceleration
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"Speed after increases: {new_car.current_speed} km/h")
new_car.accelerate(-200)

# Emergency brake
print(f"Speed after emergency brake: {new_car.current_speed} km/h")

# Drive Method
new_car.current_speed = 60
new_car.travelled_distance = 2000
new_car.drive(1.5)
print(f"New distance after 1.5 hours: {new_car.travelled_distance} km")


# Car list
cars = []

# 10 Cars
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_s = random.randint(100, 200)
    cars.append(Car(reg_num, max_s))

# Start the race loop
# Create Race
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

# Race loop
while not race.race_finished():
    hours += 1
    race.hour_passes()

    # Print every 10 hours
    if hours % 10 == 0:
        race.print_status()

# Final result
print("\n🏆 FINAL RESULT 🏆")
race.print_status()