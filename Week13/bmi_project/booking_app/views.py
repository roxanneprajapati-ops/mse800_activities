import json
from pathlib import Path
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
BOOKING_FILE = BASE_DIR / 'bookings.json'


def load_bookings():
    if BOOKING_FILE.exists():
        try:
            with open(BOOKING_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_bookings(bookings):
    with open(BOOKING_FILE, 'w') as file:
        json.dump(bookings, file, indent=4)


def book_appointment(request):
    booking_message = None
    message_type = None
    bookings = load_bookings()

    if request.method == 'POST':
        student_name = request.POST.get('student_name', '').strip()
        booking_date = request.POST.get('booking_date', '').strip()
        booking_time = request.POST.get('booking_time', '').strip()

        # Validation: empty fields
        if not student_name or not booking_date or not booking_time:
            booking_message = 'Please fill in all fields.'
            message_type = 'error'

        else:
            # Normalize name
            student_name = student_name.title()

            # Check duplicate (same date + time)
            duplicate = False
            for booking in bookings:
                if (
                    booking.get('booking_date') == booking_date and
                    booking.get('booking_time') == booking_time
                ):
                    duplicate = True
                    break

            if duplicate:
                booking_message = 'This time slot is already booked. Please choose another time.'
                message_type = 'error'

            else:
                # Save booking
                new_booking = {
                    'student_name': student_name,
                    'booking_date': booking_date,
                    'booking_time': booking_time,
                }

                bookings.append(new_booking)
                save_bookings(bookings)

                booking_message = 'Appointment booked successfully.'
                message_type = 'success'

                # Reload bookings to reflect latest data
                bookings = load_bookings()

    return render(request, 'booking_app/book_appointment.html', {
        'booking_message': booking_message,
        'message_type': message_type,
        'bookings': bookings,
    })