""" La clase solo tiene aquellos atributos que se quieren almacenar en la base de datos. ES SOLO UN CONTENEDOR"""

class UserVO:
    def __init__(self, idUser = None, nombre = None, apellido1 = None, apellido2 = None, email = None):
        self._idUser = idUser 
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._email = email

    def getIdUser(self):
        return self._idUser

    def setIdUser(self, idUser):
        self._idUser = idUser

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getApellido1(self):
        return self._apellido1

    def setApellido1(self, apellido1):
        self._apellido1 = apellido1

    def getApellido2(self):
        return self._apellido2

    def setApellido2(self, apellido2):
        self._apellido2 = apellido2

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def toString(self):
        return "UserVO{" + "DNI=" + str(self._idUser) + ", nombre='" + self._nombre + "', apellido1='" + self._apellido1 + "', apellido2='" + self._apellido2 + "', email='" + self._email + "'}"

    def __str__(self):
        return self.toString()