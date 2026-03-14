import json
from pathlib import Path
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
BOOKING_FILE = BASE_DIR / 'bookings.json'


def load_bookings():
    if BOOKING_FILE.exists():
        with open(BOOKING_FILE, 'r') as file:
            return json.load(file)
    return []


def save_bookings(bookings):
    with open(BOOKING_FILE, 'w') as file:
        json.dump(bookings, file, indent=4)


def book_appointment(request):
    booking_message = None
    bookings = load_bookings()

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')

        new_booking = {
            'student_name': student_name,
            'booking_date': booking_date,
            'booking_time': booking_time,
        }

        bookings.append(new_booking)
        save_bookings(bookings)
        booking_message = 'Appointment booked successfully.'
        bookings = load_bookings()

    return render(request, 'booking_app/book_appointment.html', {
        'booking_message': booking_message,
        'bookings': bookings,
    })