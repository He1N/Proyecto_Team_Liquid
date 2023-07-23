import mysql.connector

#Abrir conexion a la base de datos
class database:
	def __init__(self):
		self.connection = mysql.connector.connect( 
	        host = 'localhost',
	        port = 3306,
	        user = 'root',
	        password = '',
	        db = 'registro_academico'
	    )
		self.cursor = self.connection.cursor()
