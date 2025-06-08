# Given the empty dictionary


attendees = dict()

# Ask the user for an integer
attendee_count = int(input("How many attendees? "))

for names in range (attendee_count):
        attendee_name= input("Please Enter names:")
        attendee_task= input("Please Enter task:")
        attendees[attendee_name]= attendee_task
print(attendees)

# Based on the attendee_count, ask the user for that many attendee names and task
#   attendee name:
#   attendee task:
#   attendee name:
#   attendee task:
#   attendee name:
#   attendee task:
# ...

# Append each input in attendees and print attendees

