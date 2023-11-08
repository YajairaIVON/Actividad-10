from modelo.errores import NoTienePalabraSecretaError
class ReglaValidacionCalisto:
    
    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()
        return True

    def contiene_calisto(self, clave):
        return 'calisto' in clave.lower()