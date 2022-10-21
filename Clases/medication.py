import sqlite3
from Clases.urgency import Urgency


class Medication:
    '''
    Representa las medicaciones que se
    utilizan en un servicio de urgencias
    '''

    def __init__(self, connection, urgency, name=None, dosage=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency
        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('''El atributo Urgency debe ser
            un objeto de tipo Urgency''')
        self.__name = name
        self.__dosage = dosage

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        if self.__name is not None:
            string += f'Nombre: {self.__name}\n'
        if self.__dosage is not None:
            string += f'Dosis: {self.__dosage}\n\n'
        string += '----------------------------------------------'
        return string

    def setName(self, newName):
        self.__name = newName

    def setDosage(self, newDosage):
        self.__dosage = newDosage

    def save(self):
        '''
        Añade una nueva medicación a la base de datos.
        '''

        query = 'INSERT INTO Medication '
        query += '(urgency, name, dosage) '
        query += 'VALUES (?, ?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__name,
            self.__dosage,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una oxigenoterapia de la base de datos.
        '''

        query = 'SELECT name, dosage '
        query += 'FROM Medication '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__name = row["name"]
        self.__dosage = row["dosage"]

    def update(self):
        '''
        Actualiza los datos de una oxigenoterapia
        existente en la base de datos.
        '''

        query = 'UPDATE Medication '
        query += 'SET name = ?, '
        query += 'dosage = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__name,
            self.__dosage,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una oxigenoterapia existente en la base de datos.
        '''

        query = 'DELETE FROM Medication WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        self.__connection.commit()
