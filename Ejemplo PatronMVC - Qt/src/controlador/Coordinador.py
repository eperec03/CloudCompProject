from src.modelo.vo.UserVO import UserVO


class Coordinador:
    def __init__(self):
      self._model = None
      #Puede tener tantas referencias a ventanas como controle
      self._viewRegistro = None
      
    def getModel(self):
       return self._model
    
    def setModel(self, model):
       self._model = model
    
    #Se añade para cada ventana
    def getViewRegistro(self):
       return self._viewRegistro
    
    def setViewRegistro(self, view):
       self._viewRegistro = view
    
    ##############################################

    def registrarUsuario(self, usuario: UserVO) -> None:
       self._model.validar_registro(usuario)