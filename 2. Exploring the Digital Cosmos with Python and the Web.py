# Task 1
# The follwing code is what I used in the command terminal
# 
# python -m venv myenv
# myenv\Scripts\activate
# pip install requests


# Task 2
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    # Process each planet's information
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            print(f"Planet: {name}, Mass: {mass} x 10^{planet.get('mass', {}).get('massExponent', '')} kg, Orbit Period: {orbit_period} days")

fetch_planet_data()
