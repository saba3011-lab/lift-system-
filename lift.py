
print(" Welcome to Arfa Lift!")

current_floor = 1   

while True:
    requested_floor = int(input("Enter floor (1 to 14): "))

    if requested_floor == 0:
        print(" 0 is not a valid floor. Please select between 1 and 14.")
        continue
    elif 1 <= requested_floor <= 14:
        if requested_floor == current_floor:
            print("Lift is already on this floor.")
            print(" Doors opening...")
            print(" Doors closing...")
        else:
            direction = "Down" if requested_floor < current_floor else "Up"
            arrow = "<" if direction == "Down" else ">"

            print(f"Lift moving to floor {requested_floor}...")
            print(f"{arrow} Going {direction}")

            step = 1 if direction == "Up" else -1
            for floor in range(current_floor + step, requested_floor + step, step):
                print(f"Passing floor {floor}...")

            current_floor = requested_floor          
            print(f"Lift has arrived at floor {current_floor}.")
            print(" Door opening...")
            print(" Door closing...")

    else:
        print(" Invalid floor! Please choose between 1 and 14.")
