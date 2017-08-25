#!/usr/bin/python
#coding: utf-8

__author__ = "Lucas Gomes"
__date__ = "02/07/2017"

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth
from flask import render_template
from pygal.style import NeonStyle

import smtplib
import mysql.connector
import subprocess
import os
import ConfigParser
import time
import sys
import pygal


app = Flask(__name__)

def abre_mysql():
	cnx = mysql.connector.connect(
	user = 'root',
	password = 'gomes',
	host = 'localhost',
	database = 'PJI3'
	)
	cr = cnx.cursor()
	return (cr,cnx)

def fecha_mysql(cr, cnx):
	cr.close()
	cnx.close()

def recebe_bits():
	#Receber os bits da serial
	bits = '7.5'
	return bits


@app.route('/graficos/')
def cria_grafico():
	try:
		graph_data = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)
		graph_data.title = 'Browser usage evolution (in %)'
		graph_data.add('A', [1, 3,  5, 16, 13, 3,  7])
		graph_data.add('B', [5, 2,  3,  2,  5, 7, 17])
		graph_data.add('C', [6, 10, 9,  7,  3, 1,  0])
		graph_data.add('D', [2,  3, 5,  9, 12, 9,  5])
		graph_data.add('E', [7,  4, 2,  1,  2, 10, 0])
		
		graph_data = graph_data.render_data_uri()
		return render_template("graficos.html", graph_data = graph_data)
	except Exception, e:
		return(str(e))



#########################################################################
#curl -i -H "Content-Type: application/json" -X POST -d '{"idMedicao":"1"}' http://localhost:5011/inserir

@app.route('/inserir', methods=['POST'])
def inserir_valores_pico():

		a1 = request.json['idMedicao']
		bits = recebe_bits()
		query = "INSERT INTO Medicoes VALUES (0,NOW(),'"+str(bits)+"')"
		(cr,cnx) = abre_mysql()
		cr.execute(query)
		cnx.commit()
		#fecha_mysql(cr,cnx)
		return make_response(jsonify({'Feito':a1}), 201)

#########################################################################
### Função para listar produtos cadastrados ###
# Acessando via linha de comando:  curl -i http://localhost:5011/retirar

@app.route('/retirar', methods=['GET'])
def obtem_cardapio():
    query = "SELECT idMedicao,dataMedicao, valorMedicao FROM Medicoes"

    (cr,cnx) = abre_mysql()
    cr.execute(query)
    result = cr.fetchall()
    fecha_mysql(cr,cnx)

    medicoes = []
    for c in result:
        med = {
            'idMedicao': c[0],
            'dataMedicao': c[1],
            'valorMedicao': c[2]}
        medicoes.append(med)
    return jsonify({'med': medicoes})

if __name__ == "__main__":
    print "Servidor no ar!"
    app.run(host="0.0.0.0", port=5011, debug=True)


