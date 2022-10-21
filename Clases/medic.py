import sqlite3


class Medic:
    '''
    Representa los médicos que trabajan
    en servicio de urgencias
    '''

    def __init__(self, connection, npc, name=None,
    surnames=None, specialty=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        if not isinstance(npc, int):
            raise TypeError("El npc debe ser número entero")
        else:
            self.__npc = npc
        self.__name = name
        self.__surnames = surnames
        self.__specialty = specialty

    def __str__(self):
        string = f'\nNPC: {self.__npc}\n'
        if self.__name is not None:
            string += f'Nombre: {self.__name} \n'
        if self.__surnames is not None:
            string += f'Apellidos: {self.__surnames}\n'
        if self.__specialty is not None:
            string += f'Especialidad: {self.__specialty}\n'
        string += '----------------------------------------------'
        return string

    def getNPC(self):
        return self.__npc

    def getName(self):
        return self.__name

    def getSurnames(self):
        return self.__surnames

    def getSpecialty(self):
        return self.__specialty

    def setName(self, newName):
        self.__name = newName

    def setSurnames(self, newSurnames):
        self.__surnames = newSurnames

    def setSpecialty(self, newSpecialty):
        self.__specialty = newSpecialty

    def save(self):
        '''
        Añade un nuevo médico a la base de datos.
        '''

        query = 'INSERT INTO Medic (npc, name, '
        query += 'surnames, specialty) '
        query += 'VALUES (?, ?, ?, ?)'
        values = (
            self.__npc,
            self.__name,
            self.__surnames,
            self.__specialty,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria un médico de la base de datos.
        '''

        query = 'SELECT name, surnames, specialty '
        query += 'FROM Medic '
        query += 'WHERE npc = ?'
        self.__cursor.execute(query, (self.__npc,))
        row = self.__cursor.fetchone()
        self.__name = row["name"]
        self.__surnames = row["surnames"]
        self.__specialty = row["specialty"]

    def update(self):
        '''
        Actualiza los datos de un médico existente en la base de datos.
        '''

        query = 'UPDATE Medic SET name = ?, '
        query += 'surnames = ?, specialty = ? '
        query += 'WHERE npc = ?'
        values = (
            self.__name,
            self.__surnames,
            self.__specialty,
            self.__npc,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra un médico existente en la base de datos.
        '''

        query = 'DELETE FROM Medic WHERE npc = ?'
        self.__cursor.execute(query, (self.__npc,))
        self.__connection.commit()
