import sqlite3
from Clases.urgency import Urgency


class OxygenTherapy:
    '''
    Representa las oxigenoterapias que se
    realizan en un servicio de urgencias
    '''

    def __init__(self, connection, urgency, therapy=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency
        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('''El atributo Urgency debe ser
            un objeto de tipo Urgency''')
        self.__therapy = therapy

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        if self.__therapy is not None:
            string += f'Terapia: {self.__therapy}\n\n'
        string += '----------------------------------------------'
        return string

    def setTherapy(self, newTherapy):
        self.__therapy = newTherapy

    def save(self):
        '''
        Añade una nueva oxigenoterapia a la base de datos.
        '''

        query = 'INSERT INTO Oxygen_therapy '
        query += '(urgency, therapy) '
        query += 'VALUES (?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__therapy
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una oxigenoterapia de la base de datos.
        '''

        query = 'SELECT therapy '
        query += 'FROM Oxygen_therapy '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__therapy = row["therapy"]

    def update(self):
        '''
        Actualiza los datos de una oxigenoterapia
        existente en la base de datos.
        '''

        query = 'UPDATE Oxygen_therapy '
        query += 'SET therapy = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__therapy,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una oxigenoterapia existente en la base de datos.
        '''

        query = 'DELETE FROM Oxygen_therapy WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        self.__connection.commit()
