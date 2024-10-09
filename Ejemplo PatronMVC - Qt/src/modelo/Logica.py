import tkinter as tk
from tkinter import messagebox
from src.modelo.vo.UserVO import UserVO
from src.modelo.dao.UserDao import UserDao
from src.controlador.Coordinador import Coordinador

class Logica:
    def __init__(self):
        self._mi_coordinador = None

    def set_coordinador(self, mi_coordinador: Coordinador) -> None:
        self._mi_coordinador = mi_coordinador

    def validar_registro(self, mi_persona: UserVO):
        if '@' in mi_persona.getEmail():
            mi_persona_dao = UserDao()
            mi_persona_dao.insertUsuario(mi_persona)
        else:
            messagebox.showwarning("Advertencia", "El email no es válido")
