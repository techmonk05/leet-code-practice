command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started...ready to go")
    elif command == "stop":
        print("The car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop -  to stop the car
        quit - to quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I dont understand that!")