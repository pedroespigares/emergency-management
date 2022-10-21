import sqlite3
from Clases.urgency import Urgency


class Analysis:
    '''
    Representa las analíticas que se
    realizan en un servicio de urgencias
    '''

    def __init__(self, connection, urgency, petition,
    hemoglobine=None, oxygen=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__urgency = urgency

        if urgency is not None and not isinstance(self.__urgency, Urgency):
            raise TypeError('El atributo Urgency debe ser un objeto de tipo Urgency')
        
        if not isinstance(petition, int):
            raise TypeError("La petición debe ser número entero")
        else:
            self.__petition = petition

        if hemoglobine is not None and not isinstance(hemoglobine, int):
            raise TypeError("La hemoglobina debe ser número entero")
        else:
            self.__hemoglobine = hemoglobine

        if oxygen is not None and not isinstance(oxygen, int):
            raise TypeError("El oxígeno debe ser número entero")
        else:
            self.__oxygen = oxygen

    def __str__(self):
        string = f'\nUrgencia: {self.__urgency.getEpisode()}\n'
        string += f'Petición: {self.__petition}\n'
        if self.__hemoglobine is not None:
            string += f'Hemoglobina: {self.__hemoglobine} g/dL\n'
        if self.__oxygen is not None:
            string += f'Oxígeno: {self.__oxygen} mm Hg\n\n'
        string += '----------------------------------------------'
        return string

    def setPetition(self, newPetition):
        self.__petition = newPetition

    def setHemoglobine(self, newHemoglobine):
        self.__hemoglobine = newHemoglobine

    def setOxygen(self, newOxygen):
        self.__oxygen = newOxygen

    def getUrgency(self):
        return self.__urgency

    def getOxygen(self):
        return self.__oxygen

    def getHemoglobine(self):
        return self.__hemoglobine

    def save(self):
        '''
        Añade una nueva analítica a la base de datos.
        '''

        query = 'INSERT INTO Analysis (urgency, petition, '
        query += 'hemoglobine, oxygen) '
        query += 'VALUES (?, ?, ?, ?)'
        values = (
            self.__urgency.getEpisode(),
            self.__petition,
            self.__hemoglobine,
            self.__oxygen,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria una analítica de la base de datos.
        '''

        query = 'SELECT petition, hemoglobine, '
        query += 'oxygen FROM Analysis '
        query += 'WHERE urgency = ?'
        self.__cursor.execute(query, (self.__urgency.getEpisode(),))
        row = self.__cursor.fetchone()
        self.__petition = row["petition"]
        self.__hemoglobine = row["hemoglobine"]
        self.__oxygen = row["oxygen"]

    def update(self):
        '''
        Actualiza los datos de una analítica existente en la base de datos.
        '''

        query = 'UPDATE Analysis SET petition = ?, '
        query += 'hemoglobine = ?, oxygen = ? '
        query += 'WHERE urgency = ?'
        values = (
            self.__petition,
            self.__hemoglobine,
            self.__oxygen,
            self.__urgency.getEpisode(),
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una analítica existente en la base de datos.
        '''

        query = 'DELETE FROM Analysis WHERE petition = ?'
        self.__cursor.execute(query, (self.__petition,))
        self.__connection.commit()
