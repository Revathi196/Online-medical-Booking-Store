from medical_booking_system import MedicalBookingSystem

def main():
    system = MedicalBookingSystem()

    while True:
        print("\n--- Medical Booking System ---")
        print("1. Add a new doctor")
        print("2. View available doctors")
        print("3. Book an appointment")
        print("4. Cancel an appointment")
        print("5. View booked appointments")
        print("6. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            name = input("Enter doctor's name: ")
            specialty = input("Enter doctor's specialty: ")
            system.add_doctor(name, specialty)

        elif choice == "2":
            system.view_doctors()

        elif choice == "3":
            patient_name = input("Enter patient's name: ")
            doctor_id = int(input("Enter doctor's ID: "))
            appointment_time = input("Enter appointment time (YYYY-MM-DD HH:MM): ")
            system.book_appointment(patient_name, doctor_id, appointment_time)

        elif choice == "4":
            patient_name = input("Enter patient's name: ")
            doctor_id = int(input("Enter doctor's ID: "))
            appointment_time = input("Enter appointment time (YYYY-MM-DD HH:MM): ")
            system.cancel_appointment(patient_name, doctor_id, appointment_time)

        elif choice == "5":
            system.view_appointments()

        elif choice == "6":
            print("Thank you for using the Medical Booking System. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
