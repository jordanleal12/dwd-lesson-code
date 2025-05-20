command = input("Enter 'start', 'stop', or 'pause': ")

match command.lower():
    case "start":
        print("Process starting...")
    case "stop":
        print("Process stopping...")
    case "pause":
        print("Pausing process")
    case _:
        print("Error - check if input is correct")
