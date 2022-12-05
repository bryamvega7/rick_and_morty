from pymongo import MongoClient

conexion = MongoClient()

conexion = MongoClient('localhost', 27017)

db = conexion['rickandmorty'] #bd nombre
