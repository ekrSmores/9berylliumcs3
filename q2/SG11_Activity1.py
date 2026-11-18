class Patient:  #Parent
    def __init__(self, name: str, bill_amount: int):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount: int):
        if bill_amount < 0:
            raise ValueError("Amount can't be negative.")

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: int):
        super().__init__(name, bill_amount)
      
    def calculate_bill(self):
        return self.bill_amount * 0.8

    def display_patient_type(self):
        return "Patient Type: Senior Citizen"

class PhilHealthPatient(Patient):
    def __init__(self, name: str, bill_amount: int):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.bill_amount * 0.85

    def display_patient_type(self):
        return "Patient Type: PhilHealth Member"

pat1 = Patient("Juan Dela Cruz", 15000.00)
pat2 = SeniorPatient("Maria Santos", 15000.00)
pat3 = PhilHealthPatient("Pedro Reyes", 15000.00)

#TEST
print("Hospital Billing System")
print("-----------------------")
print(f'Patient Name: {pat1.get_name()}')
print(f"{pat1.display_patient_type()}")
print(f'Original Bill: ₱{pat1.get_bill_amount()}')
print(f'Final Bill: ₱{pat1.calculate_bill()}')
print("-----------------------")

print(f'Patient Name: {pat2.get_name()}')
print(f"{pat2.display_patient_type()}")
print(f'Original Bill: ₱{pat2.get_bill_amount()}')
print(f'Final Bill: ₱{pat2.calculate_bill()}')
print("-----------------------")

print(f'Patient Name: {pat3.get_name()}')
print(f"{pat3.display_patient_type()}")
print(f'Original Bill: ₱{pat3.get_bill_amount()}')
print(f'Final Bill: ₱{pat3.calculate_bill()}')
