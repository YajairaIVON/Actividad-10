from abc import ABC, abstractmethod
from modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
                           NoTieneLetraMinusculaError, NoTieneNumeroError

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave)-> bool:
        pass

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError()

    def _contiene_mayuscula(self, clave):
        if not any(char.isupper() for char in clave):
            raise NoTieneLetraMayusculaError()

    def _contiene_minuscula(self, clave):
        if not any(char.islower() for char in clave):
            raise NoTieneLetraMinusculaError()

    def _contiene_numero(self, clave):
        if not any(char.isdigit() for char in clave):
            raise NoTieneNumeroError()
    

    