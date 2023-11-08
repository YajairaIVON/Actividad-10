class ValidadorError(Exception):
    pass

class NoCumpleLongitudMinimaError(ValidadorError):
    def __init__(self, mensaje="La contraseña no cumple con la longitud mínima requerida (más de 8 caracteres)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class NoTieneLetraMayusculaError(ValidadorError):
    def __init__(self, mensaje="La contraseña no contiene al menos una letra mayúscula."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class NoTieneLetraMinusculaError(ValidadorError):
    def __init__(self, mensaje="La contraseña no contiene al menos una letra minúscula."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class NoTieneNumeroError(ValidadorError):
    def __init__(self, mensaje="La contraseña no contiene al menos un número."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class NoTieneCaracterEspecialError(ValidadorError):
    def __init__(self, mensaje="La contraseña no contiene al menos un caracter especial (@, _, #, $ o %)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class NoTienePalabraSecretaError(ValidadorError):
    def __init__(self, mensaje="La contraseña no contiene la palabra secreta requerida (calisto con al menos dos letras en mayúscula, pero no todas)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)