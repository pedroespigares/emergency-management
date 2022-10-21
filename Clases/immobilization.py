import sqlite3
from Clases.urgency import Urgency


class Immobilization:
    '''
    Representa las inmobilizaciones que se
    realizan en un servicio de urgencias
    '''

    def __init__(self, connection, urgency, type=None, place=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency
        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('''El atributo Urgency debe ser
            un objeto de tipo Urgency''')
        self.__type = type
        self.__place = place

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        if self.__type is not None:
            string += f'Tipo: {self.__type}\n'
        if self.__place is not None:
            string += f'Lugar: {self.__place}\n\n'
        string += '----------------------------------------------'
        return string

    def setType(self, newType):
        self.__type = newType

    def setPlace(self, newPlace):
        self.__place = newPlace

    def save(self):
        '''
        Añade una nueva inmobilización a la base de datos.
        '''

        query = 'INSERT INTO Immobilization '
        query += '(urgency, type, place) '
        query += 'VALUES (?, ?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__type,
            self.__place,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una inmobilización de la base de datos.
        '''

        query = 'SELECT type, place '
        query += 'FROM Immobilization '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__type = row["type"]
        self.__place = row["place"]

    def update(self):
        '''
        Actualiza los datos de una inmobilización
        existente en la base de datos.
        '''

        query = 'UPDATE Immobilization '
        query += 'SET type = ?, place = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__type,
            self.__place,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una inmobilización existente en la base de datos.
        '''

        query = 'DELETE FROM Immobilization WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        self.__connection.commit()
