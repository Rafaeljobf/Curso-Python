# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
# from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

string_json = '''
{
    "title": "O Senhor Dos Anéis: A Sociedade Do Anel",
    "original_title": "The Lord of The Rings: the Fellowship of The Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": [
        "Frodo",
        "Sam",
        "Gandalf",
        "Legolas",
        "Boromir"
    ],
    "budget": null
}
'''

movie: Movie = json.loads(string_json)
# pprint(movie)
# print(movie['title'])
# print(movie['characters'][2])
# print(movie['is_movie'])
json_string = json.dumps(movie, ensure_ascii=False, indent=4)
print(json_string)

# testar jogar a string num arquivo json

with open('aula_2_json.json', 'w+') as arquivo:
    arquivo.write(json_string)