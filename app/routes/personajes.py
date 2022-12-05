from flask import Blueprint,render_template,redirect,url_for
from app.db import db
from app.models.personajes import Personajes
import requests

personajes_ruta = Blueprint('personajes_ruta',__name__)


rickandmortyapi = "https://rickandmortyapi.com/api/character?page="



def api_get_request_character(num_page):
    return requests.get(rickandmortyapi+num_page).json()

def get_character_from_response(response_character):
    
    for i in response_character['results']:
        #print(i)
        nuevo_personaje = Personajes(i['name'])
        db.personajes.insert_one(nuevo_personaje.to_json)
        #print ("Personajes: ", i['name'])
    #print ("Personajes: ", response_character['results']['name'])
    
def get_info_from_character(num_page):
    response_character = api_get_request_character(num_page)
    #print ("Pagina : ",num_page)
    get_character_from_response(response_character) 
    

@personajes_ruta.route('/crear-personajes')
def insert():
    for i in range (1,22):
        #print(i)
        
        get_info_from_character(str(i))
        
        

#num_page=str(input("Numero de pagina: "))

#get_info_from_character(num_page)




@personajes_ruta.route('/') #Mostrar la tabla
def index():
    personajes = db.personajes.find()
    return render_template('index.html',personajes=personajes)






#@personajes_ruta.route('/crear-personaje',methods=['POST','GET']) #Crear un libro
#def guardar_personaje():
        #
#        db.personaje.insert_one(nuevo_personaje.to_json())

    