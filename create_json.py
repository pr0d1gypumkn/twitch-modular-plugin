import json

agents = []

game_name = input("Enter the name of the game file you want to create or modify: ")
filename = f"{game_name[0:3].lower()}_agents.json"

while True:
    name = input("Enter agent name (or 'q' to quit): ")
    if name == 'q':
        break

    role = input("Enter agent role: ")
    active = input("Enter agent active status (True/False): ")

    agent = {
        'name': name.lower(),
        'role': role.lower(),
        'active': active.lower()
    }



    agents.append(agent)
    
# Ask user if they want to append to existing agents.json or create a new one
option = input("Do you want to append to existing agents.json? (y/n): ")
if option.lower() == 'y':
    previous_agents = []
    try:
        with open(filename, 'r') as file:
            previous_agents = json.load(file)
            previous_agents = previous_agents["agents"]
            agent_names = [agent['name'].lower() for agent in agents]
            previous_agents = [agent for agent in previous_agents if agent["name"].lower() not in agent_names]
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        pass
    agents.extend(previous_agents)
roles = list({v['role'].lower(): v for v in agents}.values())
game_info = {
    "name": game_name,
    "roles": [role['role'] for role in roles],
    "agents": agents
}
with open(filename, 'w') as file:
    json.dump(game_info, file)