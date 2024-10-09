from jaydebeapi import Error
from typing import List
from src.modelo.vo.UserVO import UserVO
from src.modelo.conexion.Conexion import Conexion
from src.modelo.dao.UserInterface import UserInterface

class UserDao(UserInterface, Conexion):
    #Todas las operaciones CRUD que sean necesarias
    SQL_SELECT = "SELECT DNI, nombre, primer_apellido, segundo_apellido, email FROM Usuarios"
    SQL_INSERT = "INSERT INTO Usuarios(DNI, nombre, primer_apellido, segundo_apellido, email) VALUES (?, ?, ?, ?, ?)"

    def getUsuarios(self) -> List[UserVO]:
        conexion = self.getConnection()
        conn = None
        cursor = None
        usuarios = []

        try:
            if conexion:
                conn = conexion             
            else:
                print("La base de datos no esta disponible")            
            #Crea un objeto para poder ejecutar consultas SQL sobre la conexión abierta
            cursor = conn.cursor()
            #Ejecuta la consulta SQL
            cursor.execute(self.SQL_SELECT)
            #Obtiene todas las filas resultantes de la consulta
            rows = cursor.fetchall()
            #Itera sobre todas las filas
            for row in rows:
                idUser, nombre, apellido1, apellido2, email = row
                #Crea un objeto UserVO para cada fila idUser, nombre, apellido1, apellido2, email
                usuario = UserVO()
                usuario.setIdUser(idUser)
                usuario.setNombre(nombre)
                usuario.setApellido1(apellido1)
                usuario.setApellido2(apellido2)
                usuario.setEmail(email)
                usuarios.append(usuario)

        except Error as e:
            print("Error al seleccionar usuarios:", e)
        #Se ejecuta siempre
        finally:
            if cursor:
                #Cierra el cursor para liberar recursos
                cursor.close()

        self.closeConnection(conexion)
        return usuarios
    

    def insertUsuario(self, usuario: UserVO) -> int:
        conexion = self.getConnection()
        conn = None
        cursor = None
        rows = 0

        try:
            if conexion:
                conn = conexion 
            
            else:
                print("La base de datos no esta disponible")
            cursor = conn.cursor()
            cursor.execute(self.SQL_INSERT, (usuario.getIdUser(), usuario.getNombre(), usuario.getApellido1(), usuario.getApellido2(), usuario.getEmail()))
            
            #Asegurarse de que esos cambios se hagan permanentes: conn.commit(). Si conn.autocommit = True no es necesario llamar explícitamente a conn.commit() después de cada inserción, ya que la base de datos confirma automáticamente cada instrucción.
            
            #Devuelve 1 si la inserción fue exitosa
            rows = cursor.rowcount

        except Error as e:
            print("Error al insertar usuario:", e)

        finally:
            if cursor:
                cursor.close()

        self.closeConnection(conexion)

        return rows