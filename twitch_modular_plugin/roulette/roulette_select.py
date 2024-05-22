from random import randint, shuffle as rand, shuffle
import json
import os

path = os.getenv("PATH_TO_TWITCH_MODULAR_PLUGIN")
def Roulette(game_name, roles=None, num_characters=1):
    # characters = json.load(open(f'{game_name[0:3]}_agents.json', 'r'))
    characters = json.load(open(f'{path}roulette\\val_agents.json', 'r'))
    agents = []
    if roles:
        characters = [character for character in characters if character['role'] in roles]
    for _ in range(num_characters):
        shuffle(characters)
        agents.append(characters.pop())
    return agents

if __name__ == "__main__":
    print(Roulette("valorant", roles=['controller', 'initiator'], num_characters=2))