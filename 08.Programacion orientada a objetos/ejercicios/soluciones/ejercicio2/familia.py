from persona import Persona

class Familia:
    __miembros : list
    
    def __init__(self) -> None:
        self.__miembros = []
        
    def get_miembros(self) -> list:
        return self.__miembros

    def set_miembros(self, value:list):
        self.__miembros = value.copy()
    
    def agregar_miemrbro(self, miembro : Persona) -> None:
        self.__miembros.append(miembro)
    
    def listar_miembros(self) -> None:
        for miembro in self.__miembros:
            print(f"{miembro.get_nombre()} {miembro.get_apellidos()} con {miembro.get_edad()} años pertenece a la familia.")