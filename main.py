'''Creating the functionality for the application

In this file, we are going to create the functionality for our application. There are multiple functionality. 

Functionalities: 
	1. signup
	2. login
	3. add_events
	4. show_events
	5. remove_events
	6. add_participants
	7. show_participants
	8. remove_participants

'''
from models import User, EventList, ParticipantList

'''1. signup

Creating a signup page where the user provides details like fullname, username, password and email address
'''
def signup():
	fullname = input("Enter Full Name: ")
	username = input("Enter username: ")
	password = input("Enter password: ")
	email_id = input("Enter email id: ")
	print("Created New Sign Up")

	# Creating the user
	user = User.create(fullname=fullname, username=username, password=password, email_id=email_id)


'''2. login

Helping a user to login into the database
'''
def login():
	username = input("Enter username: ")
	password = input("Enter password: ")


	for person in User.select():

		# Checking the username entered is present in the database
		if username not in 	person.username:
			print("Invalid Username. Please check the username that you have entered.")

	# Checking if the entered password is right or wrong
	for person in User.select().where(User.username == username):
		if password in person.password:	
			# If the entered password is 1, return 1, else print the message
			return 1
		else:
			print("Invalid Password. Please check the password that you have entered.")


'''3. add_events

Creating an add_events page where a user can add multiple events to the database.
'''
def add_events():
	count = int(input("Enter how many events to add: "))
	for i in range(count):
		event_name=input("Enter event: ")
		event_description = input("Enter the description of the event: ")
		fees = int(input("Enter the entry fee for the event: "))
		coordinator_name = input("Enter the coordinator name: ")
		coordinator_no = int(input("Enter the coordinator's number: "))
		event_timings = input("Enter the timings of the event: ")
		
		# Saving the entered details for the event
		event = EventList.create(event_name=event_name, description=event_description, fees=fees, coordinator_name=coordinator_name, 
			coordinator_no=coordinator_no, event_timings=event_timings )


'''4. show_events

Showing all the events which are present.
'''
def show_events():
	for event in EventList.select():
		print(event.id, event.event_name, sep=" - ")


'''5. remove_events

Removing events which are not needed for the fest.
'''
def remove_events():
	print("Here are the list of the events that are present: ")
	for event in EventList.select():
		print(f"'{event.event_name}'")

	event_name = input("Enter event name to remove: ")
	delete_event = EventList.get(event_name=event_name) 
	EventList.delete_instance(delete_event)


'''6. add_participants

Creating an add_participants page where a user can add multiple participants to the database.
'''
def add_participants():
	participant_name = input("Enter the participant name: \n")
	
	# Getting data of all the events
	for event in EventList.select():
		print(event.id , event.event_name)
	
	event = int(input("Enter the choice event name from the events list above:\n"))
	
	# Getting the event name and the entry fees for that particular event
	selected_event = EventList.get(id=event)
	event_name = selected_event.event_name
	amount = selected_event.fees

	ph_no = int(input("Enter participant's phone number: "))

	# Saving the participant details to the database
	participant = ParticipantList.create(name=participant_name, event_name=event_name, price=amount, ph_no=ph_no)


'''7. show_participants

Showing all the participants who are part of the event.
'''
def view_participants():
	for event in ParticipantList.select():
		print(event.name, event.event_name, event.price, sep=" - ")


'''8. remove_participants

Removing participants who are not part of the event.
'''
def remove_participants():
	participant_name = input("Enter participant's  full name whom you want to remember: ")
	name = ParticipantList.get(name=participant_name)
	ParticipantList.delete_instance(name)


'''
Working of the application
'''
while True:
	ch = input("Select what you want to do?\n\
1. Log In\n\
2. Sign Up \n\
3. Exit \n\
Enter your choice: ")

	if ch == "1":
		state = login()
		# Checking the user has entered the proper details
		if state == 1:
			while True:
				ch = input("1. Add Participants \n\
2. View Participants \n\
3. Remove Participants \n\
4. Add events \n\
5. Show events \n\
6. Remove events \n\
7. Log Out \n\
Enter your choice: ")
				if ch == "1":
					add_participants()
				elif ch == '2':
					view_participants()
				elif ch == '3':
					remove_participants()
				elif ch == "4":
					add_events()
				elif ch == '5':
					show_events()
				elif ch == '6':
					remove_events()
				else:
					break
	elif ch == "2":
		signup()
	else:
		break