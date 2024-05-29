from random import randint, shuffle as rand, shuffle
import json, os, glob
module_dir = os.path.dirname(__file__)  # get current directory


path = os.getenv("PATH_TO_TWITCH_MODULAR_PLUGIN")
def Roulette(game_name, roles=None, num_characters=1):
    # characters = json.load(open(f'{game_name[0:3]}_agents.json', 'r'))
    file_path = os.path.join(module_dir, f'{game_name[0:3]}_agents.json')
    try:
        characters = json.load(open(file_path, 'r'))
        character = characters["agents"]
        game_roles = characters["roles"]
        characters = [character for character in character if character['active']]
    except FileNotFoundError:
        return [{"name":{"message": "Game not yet supported", "data": [glob.glob("*_agents.json")], "response": "404 Not Found"}}]
    print(os.getcwd())
    agents = []
    if roles:
        if isinstance(roles, str):
            roles = [roles]
            roles = [role.lower() for role in roles]
            roles = [role for role in roles if role in game_roles]
        characters = [character for character in characters if character['role'].lower() in roles]
    for _ in range(num_characters):
        shuffle(characters)
        try:
            agents.append(characters.pop())
        except IndexError:
            agents.append({"name":"No more characters available"})
            break
    return agents

if __name__ == "__main__":
    print(Roulette("valorant", roles=['controller', 'initiator'], num_characters=2))