from hashlib import new
from flask import render_template, request, redirect, url_for, flash
import requests
from flask_login import login_user, login_required, logout_user, current_user
from app.blueprints.auth.forms import EditProfileForm, LoginForm, RegisterForm
from . import bp as main
from .forms import PokemonForm
from ...models import Pokemon

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@main.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    form = PokemonForm()
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        response = requests.get(url)
        if not response.ok:
            error_string = "Invalid selection, try again."
            return render_template('pokemon.html.j2', error=error_string)
        
        data = response.json()
        poke_dict={
            "name": data['name'].title(),
            "ability":data['abilities'][0]["ability"]["name"].title(),
            "base_experience":data['base_experience'],
            "attack_base_stat": data['stats'][1]['base_stat'],
            "hp_base_stat":data['stats'][0]['base_stat'],
            "defense_stat":data['stats'][2]["base_stat"],
            "photo":data['sprites']['other']['home']["front_default"]
        }
        
        print('TEST!!!!!!!!!')

        return render_template('pokemon.html.j2', pokemon=poke_dict)
        
    else:
        error = 'error'
        return render_template('pokemon.html.j2', poke=error)

@main.route('/catch_pokemon', methods=['GET', 'POST'])
@login_required
def catch_pokemon():
    form = PokemonForm()
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        response = requests.get(url)
        if not response.ok:
            error_string = "Invalid selection, try again."
            return render_template('pokemon.html.j2', error=error_string)
        
        data = response.json()
        poke_dict={
            "name": data['name'].title(),
            "ability":data['abilities'][0]["ability"]["name"].title(),
            "base_experience":data['base_experience'],
            "attack_base_stat": data['stats'][1]['base_stat'],
            "hp_base_stat":data['stats'][0]['base_stat'],
            "defense_stat":data['stats'][2]["base_stat"],
            "photo":data['sprites']['other']['home']["front_default"]
        }

        new_pokemon = Pokemon()
        new_pokemon.pokemon_to_database(poke_dict)
        new_pokemon.save_poke()
        flash('Pokemon added to database', 'success')
        
        
        return render_template('search.html.j2', pokemon=poke_dict)

    else:
        error = 'error'
        return render_template('search.html.j2', poke=error)