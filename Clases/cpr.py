import sqlite3
from Clases.urgency import Urgency


class Cpr:
    '''
    Representa las RCP que se
    realizan en un servicio de urgencias
    '''

    def __init__(self, connection, urgency, type=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency
        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('''El atributo Urgency debe
            ser un objeto de tipo Urgency''')
        self.__type = type

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        if self.__type is not None:
            string += f'Tipo: {self.__type}\n\n'
        string += '----------------------------------------------'
        return string

    def setType(self, newType):
        self.__type = newType

    def save(self):
        '''
        Añade una nueva RCP a la base de datos.
        '''

        query = 'INSERT INTO CPR '
        query += '(urgency, type) '
        query += 'VALUES (?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__type
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una RCP de la base de datos.
        '''

        query = 'SELECT type '
        query += 'FROM CPR '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__type = row["type"]

    def update(self):
        '''
        Actualiza los datos de una RCP existente en la base de datos.
        '''

        query = 'UPDATE CPR '
        query += 'SET type = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__type,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una RCP existente en la base de datos.
        '''

        query = 'DELETE FROM CPR WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        self.__connection.commit()
