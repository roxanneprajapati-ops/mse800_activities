# Student Booking System

## Overview
This is a simple booking system built using Django. It allows student to book an appointment by selecting a date and time slot.

Bookings are stored in a JSON file (`bookings.json`) instead of a database.

---

## Features
- Create a booking with:
  - Student name
  - Date
  - Time slot
- View current bookings
- Prevent duplicate bookings (same date and time)
- Display success or error messages

---

## How It Works

### 1. Booking Form
Users fill in:
- Student Name
- Booking Date
- Booking Time

### 2. Submission
When the form is submitted:
- Data is sent via POST request
- Existing bookings are loaded from `bookings.json`

### 3. Validation
The system checks:
- If the selected date and time already exist

If duplicate:
> "This time slot is already booked."

If valid:
- Booking is saved
- Success message is shown

---

## File Structure
