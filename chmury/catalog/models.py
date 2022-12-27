
from neomodel  import StringProperty,DateTimeProperty,UniqueIdProperty,IntegerProperty,RelationshipTo,RelationshipFrom
from neomodel.cardinality import *
from django_neomodel import DjangoNode
from django.forms import ModelForm

class Films(DjangoNode):
	catalog_number = IntegerProperty(required=True)
	title = StringProperty(required=True)
	year_produced = IntegerProperty(required=True)
	genre = StringProperty(required=True)
	actors = RelationshipFrom("Actors","PLAYED")
	director = RelationshipFrom("Directors","DIRECTED")
 
	def __str__(self):
		return f'{self.title} - {self.year_produced}'
	def details(self):
		return (('Gatunek: ',self.genre),)
	def url(self):
		return f'/view?films_choosment={self.title.replace(" ","+")}'

class Actors(DjangoNode):
	name = StringProperty(required=True)
	last_name = StringProperty(required=True)
	age = IntegerProperty(required=True)
	gender = StringProperty(required=True)
 
	films = RelationshipTo("Films","ACTED IN")
	friends = RelationshipTo("Actors","KNOWS")
 
	def __str__(self):
		return f"{self.name} {self.last_name}"
	def details(self):
		return (('Wiek aktora:',self.age),('Płeć: ',self.gender),)
	def url(self):
		return f'/view?actors_choosment={self.name}+{self.last_name}'


class Directors(DjangoNode):
	name = StringProperty(required=True)
	last_name = StringProperty(required=True)
	age = IntegerProperty(required=True)
	gender = StringProperty(required=True)
	movies_number = IntegerProperty(required=True)
 
	directed = RelationshipTo("Films","DIRECTED")
	reviewed = RelationshipTo("Films","REVIEWED")

	def __str__(self):
		return f"{self.name} {self.last_name}"
	def details(self):
		return (('Wiek reżysera:',self.age),('Płeć: ',self.gender),('Liczba nagranych filmów: ', self.movies_number))
	def url(self):
		return f'/view?directors_choosment={self.name}'
