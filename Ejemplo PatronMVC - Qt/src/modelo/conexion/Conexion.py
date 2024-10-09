# INSTALAR JDK 
# conda install conda-forge::openjdk -> si se usa anaconda. Recordar instalarlo en el sistema operativo que useis. Windows: https://www.oracle.com/java/technologies/downloads/#jdk22-windows
# INSTALAR EL JRE
# conda install cyclus::java-jre -> si se usa anaconda. 
# INSTALAR JayDeBeApi
# pip install JayDeBeApi
# DESCARGAR JAR del conector de la base de datos (puede ser MYSQL)
# https://dev.mysql.com/downloads/connector/j/ -> plataforma independiente para windows y en zip
# CARPETA LIB
# Dentro del proyecto, se hace una carpeta lib y se descomprime el zip anterior
# Para asegurarse de que está todo correcto, el icono del archivo mysql-connector-j-8.3.0.jar no puede ser blanco. 

import jaydebeapi

class Conexion:

    # Especifica los detalles de la conexión
    host = 'localhost'
    database = 'floristeria'
    user = 'root'
    password = 'pruebaISD2024'

    "Abre una conexión a la base de datos."
    @staticmethod
    def getConnection():
        try:
            # Cargar el driver JDBC de MySQL
            jdbc_driver = "com.mysql.cj.jdbc.Driver"
            jar_file = "./lib/mysql-connector-j-8.3.0.jar"
            return jaydebeapi.connect(jdbc_driver, f"jdbc:mysql://{Conexion.host}/{Conexion.database}", [Conexion.user, Conexion.password], jar_file)
        except Exception as e:
            print(e)
            return None

    "Cierra una conexión a la base de datos."
    @staticmethod
    def closeConnection(conn):
        try:
            conn.close()
        except Exception as e:
            print(e)

