travelers = int(input("Travelers: "))
nights = int(input("Nights: "))
accommodation_per_night = float(input("Accommodation per night (whole group): "))
transport = float(input("Transport (whole trip, whole group): "))
food_per_person_per_day = float(input("Food per person per day: "))

days = nights + 1

total_accommodation = nights * accommodation_per_night
total_food = travelers * days * food_per_person_per_day
total_trip = total_accommodation + total_food + transport
cost_per_person = total_trip / travelers

print("Total accommodation:", total_accommodation)
print("Total food:", total_food)
print("Total trip:", total_trip)
print("Cost per person:", cost_per_person)
