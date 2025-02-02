class Doctor:
    def __init__(self, name, specialty, doctor_id):
        """Initialize a doctor with name, specialty, and unique ID"""
        self.name = name
        self.specialty = specialty
        self.doctor_id = doctor_id
        self.available = True  # Assume doctor is available by default

    def __str__(self):
        """Return a string representation of the doctor"""
        return f"ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}, Available: {self.available}"

class Appointment:
    def __init__(self, patient_name, doctor, appointment_time):
        """Initialize an appointment with patient name, doctor, and appointment time"""
        self.patient_name = patient_name
        self.doctor = doctor
        self.appointment_time = appointment_time

    def __str__(self):
        """Return a string representation of the appointment"""
        return f"Patient: {self.patient_name}, Doctor: {self.doctor.name}, Time: {self.appointment_time}"

class MedicalBookingSystem:
    def __init__(self):
        """Initialize the medical booking system with doctors and appointments"""
        self.doctors = []
        self.appointments = []

    def add_doctor(self, name, specialty):
        """Add a new doctor to the system"""
        doctor_id = len(self.doctors) + 1  # Unique ID for each doctor
        doctor = Doctor(name, specialty, doctor_id)
        self.doctors.append(doctor)
        print(f"Doctor '{name}' added to the system.")

    def view_doctors(self):
        """View all doctors available in the system"""
        if not self.doctors:
            print("No doctors available.")
            return
        print("\nAvailable Doctors:")
        for doctor in self.doctors:
            if doctor.available:
                print(doctor)

    def book_appointment(self, patient_name, doctor_id, appointment_time):
        """Book an appointment with a doctor if the doctor is available"""
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor and doctor.available:
            appointment = Appointment(patient_name, doctor, appointment_time)
            self.appointments.append(appointment)
            doctor.available = False  # Mark the doctor as unavailable for this time slot
            print(f"Appointment booked for {patient_name} with Dr. {doctor.name} at {appointment_time}.")
            return True
        print("Sorry, the doctor is not available at the chosen time.")
        return False

    def cancel_appointment(self, patient_name, doctor_id, appointment_time):
        """Cancel a booked appointment"""
        for appointment in self.appointments:
            if (appointment.patient_name == patient_name and
                appointment.doctor.doctor_id == doctor_id and
                appointment.appointment_time == appointment_time):
                self.appointments.remove(appointment)
                appointment.doctor.available = True  # Make the doctor available again
                print(f"Appointment canceled for {patient_name} with Dr. {appointment.doctor.name} at {appointment_time}.")
                return True
        print("No such appointment found to cancel.")
        return False

    def view_appointments(self):
        """View all current appointments"""
        if not self.appointments:
            print("No appointments booked.")
            return
        print("\nBooked Appointments:")
        for appointment in self.appointments:
            print(appointment)

    def get_doctor_by_id(self, doctor_id):
        """Return a doctor object by its ID"""
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None
