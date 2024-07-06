# Helper function used to sort the list. This function will be the parameter of the sort() function later.
def get_event_date(event):
    return event.date


# Processing function
def current_users(events):
    events.sort(key=get_event_date)
    # Before iterating through events, we create a dictionary to store the names of the machines and users logged in.
    machines = {}
    for event in events:
        if event.machine not in machines:
            # Add new machines with empty set as the value.
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    # "Once we're done iterating through the list of events, the dictionary will contain all machines we've seen as keys. With a set containing the current users of the machines as values".
    return machines


# Printing the dictionary
def generate_report(machines):
    # To iterate over keys and values in a dictionary, we can use .items() which returns both the key and value for each pair in the dictionary.
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


# Classes are used to create user-defined data structures that can hold data and methods to operate on that data.
# This class creates objects that represent an event with specific attributes. Also known as a "contstructor" this is.
class Event:
    def __init__(
        self, event_date, event_type, machine_name, user
    ):  # The __init__ method is called automatically when a new instance (object) of the class is created.
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# events list containing Event objects that have date, type, machine, and user attributes (for testing)
events = [
    Event("2020-01-21 12:45:46", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
    Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
    Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "login", "mailserver.local", "chris"),
    Event("2020-01-21 08:20:01", "login", "webserver.local", "kyle"),
    Event("2020-01-23 11:24:35", "login", "mailserver.local", "todd"),
]

users = current_users(events)
print(users)

generate_report(users)
