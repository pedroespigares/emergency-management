import sqlite3
from Clases.urgency import Urgency


class Treatment:
    '''
    Representa los tratamientos que se
    realizan en un servicio de urgencias
    '''

    def __init__(self, connection, urgency, type=None,
    antitetanus=True, anesthesia=False):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency
        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('''El atributo Urgency debe ser
            un objeto de tipo Urgency''')
        self.__type = type
        self.__antitetanus = antitetanus
        self.__anesthesia = anesthesia

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        if self.__type is not None:
            string += f'Tipo: {self.__type}\n'
        if self.__antitetanus is not None:
            if self.__antitetanus == 0:
                string += f'Antitétano: No\n'
            elif self.__antitetanus == 1:
                string += f'Antitétano: Sí\n'
        if self.__anesthesia is not None:
            if self.__anesthesia == 0:
                string += f'Anestesia: No\n\n'
            if self.__anesthesia == 1:
                string += f'Anestesia: Sí\n\n'
        string += '----------------------------------------------'
        return string

    def setType(self, newType):
        self.__type = newType

    def setAntitetanus(self, newAntitetanus):
        self.__antitetanus = newAntitetanus

    def setAnesthesia(self, newAnesthesia):
        self.__anesthesia = newAnesthesia

    def save(self):
        '''
        Añade un nuevo tratamiento a la base de datos.
        '''

        query = 'INSERT INTO Treatment '
        query += '(urgency, type, '
        query += 'antitetanus, anesthesia) '
        query += 'VALUES (?, ?, ?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__type,
            self.__antitetanus,
            self.__anesthesia,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria un tratamiento de la base de datos.
        '''

        query = 'SELECT type, antitetanus, anesthesia '
        query += 'FROM Treatment '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__type = row["type"]
        self.__antitetanus = row["antitetanus"]
        self.__anesthesia = row["anesthesia"]

    def update(self):
        '''
        Actualiza los datos de un tratamiento existente en la base de datos.
        '''

        query = 'UPDATE Treatment '
        query += 'SET type = ?, antitetanus = ?, '
        query += 'anesthesia = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__type,
            self.__antitetanus,
            self.__anesthesia,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra un tratamiento existente en la base de datos.
        '''

        query = 'DELETE FROM Treatment WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        self.__connection.commit()
