def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"

room = {
    "A": input("Enter the Status of Room A (Clean/Dirty): ").strip().capitalize(),
    "B": input("Enter the Status of Room B (Clean/Dirty): ").strip().capitalize()
}
location = input("Enter the current location (A/B): ").strip().upper()

while True:
    print("\nVacuum Cleaner Location:", location)
    print("Room Status:", room)
    if room["A"] == "Clean" and room["B"] == "Clean":
        print("All rooms are clean. Stopping the vacuum cleaner.")
        break
    action = vacuum_agent(location, room[location])
    print("Action:", action)
    if action == "Suck":
        room[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    else:
        location = "A"
