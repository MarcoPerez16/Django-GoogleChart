from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
import json
from json import dumps, load, loads
from django.views.decorators.csrf import csrf_exempt
import ast #para diccionario
import sqlite3
from .models import Global 
from django.http import StreamingHttpResponse

def index(request):
    mydb = sqlite3.connect("db.sqlite3")
    curr = mydb.cursor()
    # Mayores tiempos jugados
    ht1 = 'Usuario'
    ht2 = 'Tiempo Jugado'
    tiemposJugados = curr.execute("SELECT username, timePlayed FROM info_Global ORDER BY timePlayed DESC")
    successtj = [[ht1 , ht2]]
    
    for x in tiemposJugados:
        successtj.append([x[0], x[1]])
    tiemposJugados = dumps(successtj)

    return render(request, 'info/index.html', {'values':tiemposJugados})