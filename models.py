'''Creating tables for the database

In this file, we are creating all the required tables for the app that we want to build. We are going to need 3 different tables to build a rough
structure of our application. The name of the three tables is going to be:
1. User
2. EventList
3. ParticipantList

Database:
	The type of the database that is being used here is called sqlite3. The name of the database is going to be: 
	event_app.db
'''
# Importing everything which is present in PeeWee to create our database tables
from peewee import *

'''
Connecting PeeWee to the database named event_app.db
The extension of the database can be either of the four which are:
1. (.db)
2. (.db3)
3. (.sqlite3)
4. (.sqlite)
'''

db = SqliteDatabase('event_app.db')


'''User : Creating User Table

Here we are creating the user table. For our User Table we need 4 different rows. They are:
1. The user's name which is given as fullname -- column name : fullname
2. The user's username -- column name: username
3. The password to log in -- column name: password
4. Email id of the user -- column name: email_id

We need to tell which type of data will be stored in the database. This is given by the different field names. Some of the field names are:
1. CharField
2. IntegerField
3. TextField

These are the ones that are used here. To learn more about the different types of data which can be stored, visit the PeeWee Documentation to know more about 
it.
'''
class User(Model):
	fullname = CharField()
	username = CharField()
	password = CharField()
	email_id = CharField()

	# Connecting the User table to the database
	class Meta:
		database = db


'''EventList : Creating the Events Table

Creating the Events table which contains the details of the different events which are present. The columns which are created are:
1. The name of the event -- column name: event_name
2. The description of the event -- column name: description
3. The event fees that needs to be paid by the participants -- column name: fees
4. The name of the incharge coordinator -- column name: coordinator_name
5. The contact details of the incharge coordinator -- column name: coordinator_no
6. The timings at which the event will be conducted -- column name: event_timings
'''

class EventList(Model):
	event_name = CharField()
	description = TextField()
	fees = IntegerField()
	coordinator_name = CharField()
	coordinator_no = IntegerField()
	event_timings = CharField()

	# Connecting the Events Table to the database
	class Meta:
		database = db


'''ParticipantList : Creating the Participants Table

The participants table contains different fields which are needed for the successful conduction of the event. The columns are:
1. The name of the participant -- column name: name
2. The name of the event in which the participant is taking part -- column name: event_name
3. The amount which the participant has paid -- column name: price
4. The contact number of the participant -- column name: ph_no
'''
class ParticipantList(Model):
	name = CharField()
	event_name = CharField()
	price = IntegerField()
	ph_no = IntegerField()

	# Connecting the Participants Table to the database
	class Meta:
		database = db


# Connecting all the tables to the database
db.connect()

# Creating the tables in the database
db.create_tables([User, ParticipantList, EventList])