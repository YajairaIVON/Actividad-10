from modelo.errores import NoTieneCaracterEspecialError

class ReglaValidacionGanimedes():
    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()
        return True

    def contiene_caracter_especial(self, clave):
        return any(char in "@_#$%" for char in clave)