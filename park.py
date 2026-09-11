# Name: Nam
# Period: Am
# Theme Park Admission & Ride Eligibility System

# Asks a few questions then uses the answers to provide receipt to a made-up theme park

print("")
print("Welcome to Joyride World!")
print("In a moment we'll have your ticket ready.")
print("Then we can see which rides you're eligible for.")
print("")

# These inputs takes answers from the user, like name or age, and stores it for later

guest_name = input("Please enter your name here: ")
guest_age = input("Please enter your age here: ")
height = input("Please enter height in inches here: ")
ticket_type = input("Did you purchase a regular or premium ticket?: ")
park_member = input("Are you a park member? Yes/No: ")
visit_with_adult = input("Are you coming with an adult? Yes/No: ")
visit_time = input("Are you coming during the morning or the evening?: ")

# This function takes the user's age and figures out the cost of a ticket for their age before the discount

def calculate_admission(age):
    if int(age) <= 4:
        price = 0
    elif int(age) <= 12:
        price = 15
    elif int(age) <= 64:
        price = 30
    else:
        price = 20
    return price

admission_price = calculate_admission(guest_age)

# Now this function takes the calculations from the last one and adds on a discount based on if they're a member and the time they go

def calculate_discount(price, member, visit_time):
    if (member == "yes" or member == "Yes") and (visit_time == "evening" or visit_time == "Evening"):
        final_price = int(price) - 10
    elif (member == "yes" or member == "Yes"):
        final_price = int(price) - 5
    elif (visit_time == "evening" or visit_time == "Evening"):
        final_price = int(price) - 3
    else:
        final_price = int(price)
    return final_price

# These few lines of code prevent the cost from going negative if a child of age 0-4 gets a discount

final_admission_price = calculate_discount(admission_price, park_member, visit_time)

if int(final_admission_price) < 0:
    final_admission_price = 0

# This function gets the age and height (in inches) of the user to determine the highest level of rides they're allowed to

def ride_level(age, height):
    if int(age) >= 16 and int(height) >= 54:
        level = "Extreme Rides"
    elif int(age) >= 12 and int(height) >= 48:
        level = "Thrill Rides"
    elif int(age) >= 8 and int(height) >= 42:
        level = "Family Rides"
    elif int(height) >= 36:
        level = "Kiddie Rides"
    else:
        level = "No Rides"
    return level

highest_ride_level = ride_level(guest_age, height)

# This final function checks the age again and if the user is going with an adult to see if they require an adult or aren't approved to enter

def check_supervision(age, visiting_with_adult):
    if int(age) < 13 and (visiting_with_adult == "No" or visiting_with_adult == "no"):
        supervision = "Adult Required"
    else:
        supervision = "Approved"
    return supervision

checked_supervision = check_supervision(guest_age, visit_with_adult)

# These four lines checks if the user has a premium ticket and if they will recieve special privilege

if ticket_type == "Premium" or ticket_type == "premium":
    ticket_status = "Ticket Perk - You have access to ride priority, free food and drinks, and exclusive events!"
else:
    ticket_status = "Your park ticket is ready!"

if ticket_type == "Premium" or ticket_type == "premium":
    end_message = "Thank you for purchasing premium. We hope to make it worthwhile for you!"
else:
    end_message = "We hope you have an amazing day!"

# Here is the final report where all of the previous calculations are put together with many print codes

def check_vip(ticket, age, member):
    if (ticket == "Premium" or ticket == "premium") and ((int(age) >= 65) or (member == "Yes" or member == "yes")):
        access = "VIP ACCESS"
    else:
        access = "STANDARD ACCESS"
    return access

guest_access = check_vip(ticket_type, guest_age, park_member)

print("")
print("------------------------------")
print("JOYRIDE WORLD PARK REPORT")
print("------------------------------")
print("")
print("GUEST INFORMATION")
print("------------------------------")
print("Guest: ", guest_name)
print("")
print("Age: ", int(guest_age))
print("Height: ", int(height), "inches")
print("Ticket: ", ticket_type)
print("Park Member: ", park_member)
print("")
print("COST")
print("------------------------------")
print("Normal Admission: $", int(admission_price))
print("Final Admission: $", int(final_admission_price))
print("")
print("ACCESS")
print("------------------------------")
print("Max Ride Level:")
print(highest_ride_level)
print("")
print("Supervision:")
print(checked_supervision)
print("")
print("Ticket:")
print(ticket_status)
print("")
print("Guest Access:")
print(guest_access)

# This last part takes the if and elif codes from line 88 to 91 to give a special message to those who purchased premium

print("------------------------------")
print(end_message)
print("------------------------------")