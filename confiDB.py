
#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        #host ="localhost",
        host ="b0ilsbp5axpf1cdf0y8e-mysql.services.clever-cloud.com",
        user ="uhwtvgcnoburkmaj",
        passwd ="6cPBd5hT6j3HSQHgDf34",
        database = "b0ilsbp5axpf1cdf0y8e"
        )
    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error en la conexion a BD")
    return mydb
     