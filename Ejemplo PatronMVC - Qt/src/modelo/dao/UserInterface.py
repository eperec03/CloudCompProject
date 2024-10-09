from typing import List
from abc import ABC, abstractmethod
from src.modelo.vo.UserVO import UserVO

""" La interface permite acceder a distintos tipos de fuentes de datos. """
class UserInterface(ABC):
    @abstractmethod
    def getUsuarios(self) -> List[UserVO]:
        """
        Recupera todos los usuarios de la base de datos.        
        Devuelve: List[UserDTO]: Una lista de objetos UserDTO.
        """
        raise NotImplementedError("Método getUsuarios no implementado")
    
    @abstractmethod
    def insertUsuario(self, usuarios: UserVO):
        """
        Inserta un nuevo usuario en la base de datos.
        Parametros requeridos: El objeto UserVO a insertar.
        Devuelve: int: 1 si fue exitoso
        """
        raise NotImplementedError("Método insertUsuario no implementado")