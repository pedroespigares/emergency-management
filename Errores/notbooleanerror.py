class NotBooleanError(Exception):
    """Indica que el valor introducido no es booleano (1 o 0)

    Atributos:
    value: valor introducido
    message:   texto informativo para el usuario final
    """

    def __init__(self, value, message="Error: Valor no booleano (0 o 1) => "):
        self.value = value
        self.message = message + str(value)
        super().__init__(self.message)
