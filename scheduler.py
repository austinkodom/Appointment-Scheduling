# Initialize the doctor's schedule using a dictionary.
# The key will be the days of the week, and the values 
# are a tuple representing appointment hours.
schedule = {
    "Monday": [(9, 10), (11, 12)],
    "Tuesday": [(10, 11)],
    "Wednesday": [],
    "Thursday": [(13, 14), (15,16)],
    "Friday": [(9, 10), (11, 12)]
}

# Declare a function to check for conflicting times.
def is_conflicting(schedule, new_app):
    for start_time, end_time in schedule:
        if not (new_app[1] < start_time or new_app[0] >= end_time):
            return True

    return False

# Declare a function to add new appointments
# adhering to all the given requirements.
def add_appointment(new_appointment):
    # Sort the schedule by the number of days by number of
    # appointments, helping us keep priority on higher numeber days
    sorted_days = sorted(schedule.keys(), key=lambda day: len(schedule[day]), reverse=True)

    for day in sorted_days:
        # Check to see if the new appointment conflicts with an existing time
        if not is_conflicting(schedule[day], new_appointment):
            schedule[day].append(new_appointment)
            schedule[day].sort()
            print(f"Appointment {new_appointment} added to {day}\n")
            return schedule

    print(f"Could not add appointment. No available times.\n")
    return schedule

# Declare a function to show the doctor's schedule.
def show_schedule(schedule):
    for day, appointments in schedule.items():
        print(f"{day}: {appointments}")
    print("\n")

# Main Function.
show_schedule(schedule)

# Create some appointments to be addeded. User input (later?).
new_appointment = (1, 2)
add_appointment(new_appointment)
show_schedule(schedule)

new_appointment2 = (3,4)
add_appointment(new_appointment2)
show_schedule(schedule)

new_appointment3 = (9, 10)
add_appointment(new_appointment3)
show_schedule(schedule)

new_appointment4 = (3,4)
add_appointment(new_appointment4)
show_schedule(schedule)

new_appointment5 = (11, 12)
add_appointment(new_appointment5)
show_schedule(schedule)

new_appointment6 = (7, 8)
add_appointment(new_appointment6)
show_schedule(schedule)
