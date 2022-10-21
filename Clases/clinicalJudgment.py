import sqlite3


class ClinicalJudgment:
    '''
    Representa los juicios clínicos,
    que indican unos códigos para los
    diferentes diagnósticos
    '''

    def __init__(self, connection, code, description=None):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
        self.__code = code
        self.__description = description

    def __str__(self):
        string = f'\nCódigo: {self.__code}\n'
        if self.__description is not None:
            string += f'Descripción: {self.__description} \n'
        string += '----------------------------------------------'
        return string

    def getCode(self):
        return self.__code

    def getDescription(self):
        return self.__description

    def setDescription(self, newDescription):
        self.__description = newDescription

    def save(self):
        '''
        Añade un nuevo juicio clínico a la base de datos.
        '''

        query = 'INSERT INTO Clinical_Judgment (code, '
        query += 'description) VALUES (?, ?)'
        values = (
            self.__code,
            self.__description,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def load(self):
        '''
        Carga en memoria un juicio clínico de la base de datos.
        '''

        query = 'SELECT description '
        query += 'FROM Clinical_Judgment '
        query += 'WHERE code = ?'
        self.__cursor.execute(query, (self.__code,))
        row = self.__cursor.fetchone()
        self.__description = row["description"]

    def update(self):
        '''
        Actualiza los datos de un juicio clínico existente en la base de datos.
        '''

        query = 'UPDATE Clinical_Judgment SET description = ? '
        query += 'WHERE code = ?'
        values = (
            self.__description,
            self.__code,
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra un juicio clínico existente en la base de datos.
        '''

        query = 'DELETE FROM Clinical_Judgment WHERE code = ?'
        self.__cursor.execute(query, (self.__code,))
        self.__connection.commit()
