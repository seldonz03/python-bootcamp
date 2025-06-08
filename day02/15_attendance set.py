attendee_names = set()

attendee_count = int(input("How many attendees?:"))

for names in range (attendee_count):
        attendee_name= input( "Please Enter names:")
        attendee_names.add(attendee_name)

print(attendee_names)
print("Winner",attendee_names.pop())


