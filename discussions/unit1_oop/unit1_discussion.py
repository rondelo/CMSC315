"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    system_name = "HomeLink"
    device_count = 0

    def __init__(self, name, location):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Device name must be a non-empty string.")
        if not isinstance(location, str) or not location.strip():
            raise ValueError("Device location must be a non-empty string.")

        self.name = name.strip()
        self.location = location.strip()
        self.is_online = False
        self.settings = {"notifications": True, "authorized_users": []}
        ParentClass.device_count += 1

    def connect(self):
        self.is_online = True
        return f"{self.name} connected to {self.system_name}."

    def display_info(self):
        status = "online" if self.is_online else "offline"
        return f"{self.name} is a device in the {self.location} and is {status}."


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    device_type = "Smart Thermostat"
    minimum_temperature = 50
    maximum_temperature = 90

    def __init__(self, name, location, target_temperature, schedule=None):
        super().__init__(name, location)
        self._target_temperature = self._validate_temperature(target_temperature)
        self.schedule = list(schedule) if schedule is not None else []

    @classmethod
    def _validate_temperature(cls, temperature):
        if isinstance(temperature, bool) or not isinstance(temperature, (int, float)):
            raise TypeError("Temperature must be a number.")
        if not cls.minimum_temperature <= temperature <= cls.maximum_temperature:
            raise ValueError(
                f"Temperature must be between {cls.minimum_temperature} and "
                f"{cls.maximum_temperature} degrees."
            )
        return temperature

    @property
    def target_temperature(self):
        return self._target_temperature

    def set_temperature(self, temperature):
        self._target_temperature = self._validate_temperature(temperature)
        return f"{self.name} is now set to {temperature} degrees."

    def add_schedule_entry(self, time, temperature, days):
        if not days:
            raise ValueError("A schedule entry must include at least one day.")
        validated_temperature = self._validate_temperature(temperature)
        self.schedule.append(
            {"time": time, "temperature": validated_temperature, "days": list(days)}
        )

    def display_info(self):
        status = "online" if self.is_online else "offline"
        return (
            f"{self.name} is a {self.device_type.lower()} in the {self.location}. "
            f"It is {status} and set to {self.target_temperature} degrees."
        )


# Student-created extension: this class uses composition to coordinate devices.
class SmartHomeSystem:
    def __init__(self, home_name):
        self.home_name = home_name
        self.devices = []

    def add_device(self, device):
        if not isinstance(device, ParentClass):
            raise TypeError("Only ParentClass devices can be added to the system.")
        if device in self.devices:
            raise ValueError(f"{device.name} is already registered.")
        self.devices.append(device)

    def connect_all(self):
        return [device.connect() for device in self.devices]

    def display_summary(self):
        if not self.devices:
            return f"{self.home_name} has no registered devices."
        return f"{self.home_name} manages {len(self.devices)} device(s)."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    living_room = ChildClass("Living Room Thermostat", "living room", 72)
    bedroom = ChildClass("Bedroom Thermostat", "bedroom", 68)

    print(f"Class access: {ChildClass.system_name}")
    print(f"Object access: {living_room.system_name}")

    living_room.firmware_version = "2.1.0"
    print("\nLiving room instance namespace:")
    print(living_room.__dict__)
    print("\nBedroom instance namespace:")
    print(bedroom.__dict__)

    class_attributes = sorted(
        attribute for attribute in ChildClass.__dict__ if not attribute.startswith("__")
    )
    print("\nChild class namespace attributes:")
    print(class_attributes)
    print(f"Parent class: {ChildClass.__bases__[0].__name__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ChildClass("Kitchen Thermostat", "kitchen", 70)
    original.add_schedule_entry("07:00", 72, ["Monday", "Tuesday"])

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new outer object but shares nested mutable objects.
    # A deep copy recursively duplicates nested objects, so later changes are isolated.
    original.schedule[0]["days"].append("Wednesday")
    original.settings["authorized_users"].append("Alex")

    print(f"Original schedule: {original.schedule}")
    print(f"Shallow-copy schedule: {shallow_copy.schedule}")
    print(f"Deep-copy schedule: {deep_copy.schedule}")
    print(f"Original settings: {original.settings}")
    print(f"Shallow-copy settings: {shallow_copy.settings}")
    print(f"Deep-copy settings: {deep_copy.settings}")
    print("The shallow copy changed with the original; the deep copy stayed independent.")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    security_camera = ParentClass("Front Door Camera", "entryway")
    print(security_camera.display_info())
    print(security_camera.connect())
    print(security_camera.display_info())

    print("\n=== Child Object and Inheritance ===")
    thermostat = ChildClass("Main Thermostat", "hallway", 71)
    print(thermostat.display_info())
    print(thermostat.connect())
    print(thermostat.set_temperature(73))
    thermostat.add_schedule_entry("22:00", 67, ["Monday", "Tuesday"])
    print(f"Schedule: {thermostat.schedule}")

    print("\n=== Student Extension and Edge Cases ===")
    home = SmartHomeSystem("Ridgley Home")
    print(home.display_summary())
    home.add_device(security_camera)
    home.add_device(thermostat)
    print(home.display_summary())

    try:
        thermostat.set_temperature(120)
    except ValueError as error:
        print(f"Handled invalid temperature: {error}")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
