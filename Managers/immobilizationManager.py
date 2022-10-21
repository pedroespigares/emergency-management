import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.immobilization import Immobilization
from Clases.urgency import Urgency


class ImmobilizationManager:
    '''
    Gestiona los objetos de la clase Immobilization en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getImmobilizationSets(self, rows):
        '''
        Crea un objeto Immobilization a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Inmovilizaciones(Immobilization)
        '''

        result = set()
        if rows is None:
            return result
        for row in rows:
            obtainedUrgency = Urgency(
                self.__connection,
                None,
                row["urgency"],
            )
            obtainedImmobilization = Immobilization(
                self.__connection,
                obtainedUrgency,
                row["type"],
                row["place"],
            )
            result.add(obtainedImmobilization)
        return result

    def getImmobilizationBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de inmovilizaciones
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, type, place '
        query += 'FROM Immobilization '
        return query

    def getAllImmobilization(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Immobilization
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Immobilization
        '''

        query = 'SELECT urgency, type, place '
        query += 'FROM Immobilization'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getImmobilizationSets(rows)

    def getImmobilizationByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Immobilization según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a Immobilization
        resultado = devolvera un conjunto de objetos tipo Immobilization
        '''

        query = self.getImmobilizationBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getImmobilizationSets(rows)

    def getImmobilizationByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Immobilization según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la urgencia
        de una inmovilización (str)
        resultado = devolvera un conjunto de objetos tipo Immobilization
        '''

        query = self.getImmobilizationBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getImmobilizationSets(rows)

    def getImmobilizationByType(self, type):
        '''
        Devuelve una coleccion de objetos tipo Immobilization segun su tipo

        type = contendrá parte del tipo de una Immobilization (str)
        resultado = devolvera un conjunto de objetos tipo Immobilization
        '''

        query = self.getImmobilizationBaseSQL()
        query += 'WHERE lower(type) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{type}%',))
        rows = self.__cursor.fetchall()
        return self.__getImmobilizationSets(rows)

    def getImmobilizationByPlace(self, place):
        '''
        Devuelve una coleccion de objetos tipo Immobilization segun su lugar

        place = contendrá parte de la zona de una Immobilization (str)
        resultado = devolvera un conjunto de objetos tipo Immobilization
        '''

        query = self.getImmobilizationBaseSQL()
        query += 'WHERE lower(place) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{place}%',))
        rows = self.__cursor.fetchall()
        return self.__getImmobilizationSets(rows)

    def deleteAllImmobilizationFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos las inmovilizaciones que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Immobilization WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
