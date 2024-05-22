import json

agents = []

filename = input("Enter the name of the file you want to create or modify: ")


while True:
    name = input("Enter agent name (or 'q' to quit): ")
    if name == 'q':
        break

    role = input("Enter agent role: ")
    active = input("Enter agent active status (True/False): ")

    agent = {
        'name': name,
        'role': role,
        'active': active
    }



    agents.append(agent)
    
# Ask user if they want to append to existing agents.json or create a new one
option = input("Do you want to append to existing agents.json? (y/n): ")
if option.lower() == 'y':
    previous_agents = []
    try:
        with open(filename, 'r') as file:
            previous_agents = json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        pass
    agents.extend(previous_agents)
    agents = list({v['name']: v for v in agents}.values())
    # Append agents list to existing JSON file
    with open(filename, 'w') as file:
        json.dump(agents, file)
else:
    # Write agents list to a new JSON file
    with open(filename, 'w') as file:
        json.dump(agents, file)
