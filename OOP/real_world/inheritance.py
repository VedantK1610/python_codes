# Single Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        pass

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_info(self):
        return f"Doctor {self.name}, Age: {self.age}, Specialization: {self.specialization}"

# Multiple Inheritance
class Patient:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id

class Billing:
    def __init__(self, total_cost):
        self.total_cost = total_cost

class Bill(Patient, Billing):
    def __init__(self, name, age, patient_id, total_cost):
        Patient.__init__(self, name, age, patient_id)
        Billing.__init__(self, total_cost)

    def display_bill(self):
        return f"Patient {self.name}, Age: {self.age}, Bill ID: {self.patient_id}, Total Cost: ${self.total_cost}"

# Multilevel Inheritance
class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

class Nurse(Staff):
    def __init__(self, name, age, staff_id, department):
        super().__init__(name, age, staff_id)
        self.department = department

    def display_info(self):
        return f"Nurse {self.name}, Age: {self.age}, Staff ID: {self.staff_id}, Department: {self.department}"

# Hierarchical Inheritance
class Administrator(Staff):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age, staff_id)
        self.role = role

    def display_info(self):
        return f"Administrator {self.name}, Age: {self.age}, Staff ID: {self.staff_id}, Role: {self.role}"

class Receptionist(Staff):
    def __init__(self, name, age, staff_id, shift):
        super().__init__(name, age, staff_id)
        self.shift = shift

    def display_info(self):
        return f"Receptionist {self.name}, Age: {self.age}, Staff ID: {self.staff_id}, Shift: {self.shift}"

# Hybrid Inheritance
class Surgeon(Doctor, Staff):
    def __init__(self, name, age, specialization, staff_id, department):
        Doctor.__init__(self, name, age, specialization)
        Staff.__init__(self, name, age, staff_id)
        self.department = department

    def display_info(self):
        return f"Surgeon {self.name}, Age: {self.age}, Specialization: {self.specialization}, Staff ID: {self.staff_id}, Department: {self.department}"

# Create instances and test
doctor = Doctor("Dr. Smith", 45, "Cardiology")
bill = Bill("Alice", 28, "B001", 5000)
nurse = Nurse("Nurse Jane", 32, "N001", "ICU")
administrator = Administrator("Admin Joe", 40, "A001", "Head of HR")
receptionist = Receptionist("Receptionist Sara", 28, "R001", "Day Shift")
# surgeon = Surgeon("Dr. Johnson", 50, "Orthopedics", "S001", "Surgery")

print(doctor.display_info())  # Single Inheritance
print(bill.display_bill())    # Multiple Inheritance
print(nurse.display_info())   # Multilevel Inheritance
print(administrator.display_info())  # Hierarchical Inheritance
print(receptionist.display_info())   # Hierarchical Inheritance
# print(surgeon.display_info())   # Hybrid Inheritance
