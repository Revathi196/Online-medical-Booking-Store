# Online Medical Booking System

This is a simple command-line-based **Medical Booking System** that allows patients to book, view, and cancel appointments with doctors. The system enables users to interact with a list of doctors, book appointments, and manage those appointments effectively.

## Features

- **Add a New Doctor**: Add doctors with specific specialties to the system.
- **View Available Doctors**: View a list of all available doctors and their specialties.
- **Book an Appointment**: Book an appointment with a doctor, specifying the patient's name and the appointment time.
- **Cancel an Appointment**: Cancel a booked appointment.
- **View Booked Appointments**: View all the appointments that have been booked.

## Files in the Repository

### 1. `medical_booking_system.py`

This file contains the core logic for managing the medical booking system:
- **`Doctor` class**: Represents a doctor with a name, specialty, and availability status.
- **`Appointment` class**: Represents an appointment with patient details, the doctor involved, and the appointment time.
- **`MedicalBookingSystem` class**: Manages doctors, appointments, and user interactions with the system. This includes functionality to add doctors, view available doctors, book/cancel appointments, and view booked appointments.

### 2. `main.py`

This file is the entry point for the system, providing a simple text-based interface for users to interact with the system:
- Allows users to:
  - Add new doctors.
  - View available doctors.
  - Book and cancel appointments.
  - View all booked appointments.
- The system uses the `MedicalBookingSystem` class to execute all actions.

## How to Run

### Step 1: Install Python
Ensure that you have Python 3.x installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Step 2: Download or Clone the Repository
Download or clone the repository to your local machine.

### Step 3: Run the System
Open your terminal, navigate to the directory where the files are located, and run the following command:

```bash
python main.py
