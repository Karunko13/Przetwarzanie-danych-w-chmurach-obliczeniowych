from asyncio.windows_events import NULL

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from catalog.models import *


def index(request):
	context = {
	"films_list": Films.nodes.all(),
	"actors_list": Actors.nodes.all(),
	"directors_list": Directors.nodes.all()
	}
	return render(request,'template_index.html',context)


def view_films(request):
	film_title = request.GET['films_choosment']
	if not film_title:
		return
	chosen_film = Films.nodes.get(title=film_title)
	return {
	'title':f'Dane: {film_title} {chosen_film.year_produced} {chosen_film.genre}'}
 
 	#,
	# 'dataset':[
	# {
	# 	'title' : 'Aktorzy',
	# 	'data':chosen_film.actors.all()
	# },
	# {
	# 	'title' : 'Reżyser',
	# 	'data':chosen_film.director.all()
	# }
	# ],
	# 	'selected' : chosen_film
	# }

def view_actors(request):
	actor_full_name = request.GET['actors_choosment'].split()
	if not actor_full_name:
		return
	actor_last_name = actor_full_name[1]
	actor_name = actor_full_name[0]
	actor = Actors.nodes.get(name=actor_name, last_name=actor_last_name)
	return {
	'title':f' Aktor {actor.name} {actor.last_name} {actor.age} {actor.gender}',
	'dataset':[
	{
		'title' : 'Grał w',
		'data':actor.films.all()
	},
	{
		'title' : 'Pracował z',
		'data' : actor.friends.all()
	}
	],
		'selected' : actor
	}
 
def view_directors(request):
	director_full_name = request.GET['directors_choosment'].split()
	if not director_full_name:
		return
	director_last_name = director_full_name[1]
	director_name = director_full_name[0]
	director = Actors.nodes.get(name=director_name, last_name=director_last_name)
	return {
	'title':f' Reżyser {director.name} {director.last_name} {director.age} {director.gender}',
	'dataset':[
	{
		'title' : 'Wyreżyserował',
		'data':director.directed.all()
	},
	{
		'title' : 'Zrecenzował',
		'data' : director.reviewed.all()
	}
	],
		'selected' : director
	}

def data_add(request):
    
    film_title = request.GET["film_title"]
    film_director = request.GET["film_director"].split()
    film_actor = request.GET["film_actor"].split()
    
    new_film = Films(catalog_number = 1, year_produced=2000, genre="Komedia", title=film_title)
    new_film.save()
    actor = Actors.nodes.get(name= film_actor[0])
    actor.films.connect(new_film)
    director = Directors.nodes.get(name = film_director[0])
    director.directed.connect(new_film)
    
    print(film_title)
    print(film_director)
    print(film_actor)

    return {}


def view(request):
	if 'films_choosment' in request.GET:
		context = view_films(request)
	elif 'actors_choosment' in request.GET:
		context = view_actors(request)
	elif 'directors_choosment' in request.GET:
		context = view_directors(request)
	elif 'film_title' in request.GET:
		context = data_add(request)
  
	return render(request,'template_view.html',context)


    