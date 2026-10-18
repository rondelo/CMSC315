# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation

The program models a small smart-home system:

- `ParentClass` represents a general smart device. It stores the device name,
  location, connection status, and settings. Its class variables track the
  shared system name and the number of devices created.
- `ChildClass` represents a smart thermostat. It inherits the shared device
  behavior, adds a temperature and schedule, overrides `display_info()`, and
  validates temperature changes. The temperature is encapsulated in the
  `_target_temperature` attribute and exposed through a read-only property.
- `demonstrate_namespaces()` shows inherited class-variable access, separate
  instance namespaces, a dynamically added instance attribute, and the child
  class namespace.
- `demonstrate_copying()` proves that a shallow copy shares nested lists and
  dictionaries while a deep copy remains independent.
- `SmartHomeSystem` is the student-created extension. It uses composition to
  register and coordinate multiple device objects.

## Error Handling and Edge Cases

Constructors reject missing or empty names and locations. Thermostat methods
raise clear exceptions for nonnumeric temperatures, values outside 50–90
degrees, and schedules with no days. The `main()` function deliberately tries
to set a temperature of 120 degrees and catches the resulting `ValueError`, so
the rest of the smart-home program continues running. It also displays an empty
system before devices are registered, demonstrating safe handling of an empty
collection.

## Running the Program

From the repository root, run:

```bash
python3 unit1_oop/unit1_discussion.py
```

The output is divided into parent object, child object, extension, namespace,
and copying sections so each required concept is easy to identify.

## Real-World Application

A smart-home platform is a practical example of object-oriented design. Every
device shares basic identity and connection behavior, while specialized devices
add their own responsibilities. A thermostat can validate temperature settings
without exposing that logic to cameras or locks. This separation makes it
possible to add new device types without rewriting the whole system.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Initial Discussion Post Draft

**Repository:** Add your GitHub repository link here before posting.

**Design approach:** My program uses a parent class for behavior shared by all
smart devices and a child thermostat class for specialized temperature and
schedule behavior. Each object maintains its own state, while class variables
hold information shared across objects. I also added a `SmartHomeSystem` class
that demonstrates composition by managing multiple device objects.

**Reflection (186 words):**

While completing this assignment, I learned how inheritance, encapsulation,
namespaces, and object copying work together in an object-oriented program. My
smart-home example uses a general device class and a thermostat subclass. This
mirrors daily systems because each device hides its settings while sharing
common connection behavior. The main challenge
was understanding why a shallow copy changed when I modified nested schedule
data. Printing each object's namespace and comparing it with a deep copy made
the shared references visible.

Procedural programming would pass device data between separate functions. OOP
instead keeps data and related behavior together, making responsibilities
clearer. Inheritance also avoids repeating
connection and status logic for every device type. Validation and exception
handling turn an invalid 120-degree thermostat request into a minor warning
rather than a system-wide failure.

A reusable base class reduces overhead and can support future locks, cameras,
and sensors. Localized changes also simplify testing and maintenance. In my
future work, I could apply these ideas to cybersecurity or Internet of Things
applications, where specialized devices must cooperate without exposing
sensitive internal state or allowing one bad input to disrupt the entire
network.
