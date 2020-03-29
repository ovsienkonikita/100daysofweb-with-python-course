from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

import requests
from flask import render_template, request

from program import app

time_now = str(datetime.today())


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Template Demo", time=time_now)


@app.route("/100Days")
def p100days():
    return render_template("100Days.html")


@app.route("/chuck")
def chuck():
    joke = get_chuck_joke()
    return render_template("chuck.html", joke=joke)


@app.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    pokemons = []
    if request.method == "POST" and "pokecolour" in request.form:
        colour = request.form.get("pokecolour")
        pokemons = get_pokemons_by_color(colour)
    return render_template("pokemon.html", pokemons=pokemons)


def get_chuck_joke():
    r = requests.get("https://api.chucknorris.io/jokes/random")
    data = r.json()
    return data["value"]


def get_pokemons_by_color(colour):
    r = requests.get("https://pokeapi.co/api/v2/pokemon-color/" + colour.lower())
    pokedata = r.json()

    with ThreadPoolExecutor(max_workers=cpu_count() * 2) as executor:
        pokemons = executor.map(requests.get, (p["url"] for p in pokedata["pokemon_species"]))

    return (pokemon.json() for pokemon in pokemons)
