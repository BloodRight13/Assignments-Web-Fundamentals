# Task 1
# The follwing code is what I used in the command terminal
# 
# python -m venv myenv
# myenv\Scripts\activate
# pip install requests


# Task 2
import requests
import json
pokemon_names = ['pikachu', 'bulbasaur', 'charmander']

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

if response.status_code == 200:
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print(f"Name: {name}")
    print("Abilities:", ", ".join(abilities))
else:
    print("Failed to retrieve data")

# Task 3

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]

        print(f"Name: {name}")
        print("Abilities:", ", ".join(abilities))
    else:
        print(f"Failed to retrieve data for {pokemon_name}")


def calculate_average_weight(pokemon_names):
    total_weight = 0
    list_count = 0
    
    for pokemon_name in pokemon_names:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        data = response.json()
        weights = data['weight']
        
        total_weight += weights
        list_count += 1

        average_weight = total_weight / list_count

        if response.status_code == 200:
            print(average_weight)
        else:
            print(f"Failed to calculate average weightfor {pokemon_names}")


for pokemon in pokemon_names:

    fetch_pokemon_data(pokemon)
    
calculate_average_weight(pokemon_names)