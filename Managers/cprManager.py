import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.cpr import Cpr
from Clases.urgency import Urgency


class CprManager:
    '''
    Gestiona los objetos de la clase Cpr en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getCprSets(self, rows):
        '''
        Crea un objeto Cpr a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Análisis(Cpr)
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
            obtainedCpr = Cpr(
                self.__connection,
                obtainedUrgency,
                row["type"],
            )
            result.add(obtainedCpr)
        return result

    def getCprBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de RCP
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, type '
        query += 'FROM CPR '
        return query

    def getAllCpr(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Cpr
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Cpr
        '''

        query = 'SELECT urgency, type '
        query += 'FROM CPR'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getCprSets(rows)

    def getCprByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Cpr según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a Cpr
        resultado = devolvera un conjunto de objetos tipo Cpr
        '''

        query = self.getCprBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getCprSets(rows)

    def getCprByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Cpr según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la
        urgencia de una reanimación (str)
        resultado = devolvera un conjunto de objetos tipo Cpr
        '''

        query = self.getCprBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getCprSets(rows)

    def getCprByType(self, type):
        '''
        Devuelve una coleccion de objetos tipo Cpr segun su tipo

        type = contendrá parte del tipo de una CPR (str)
        resultado = devolvera un conjunto de objetos tipo Cpr
        '''

        query = self.getCprBaseSQL()
        query += 'WHERE lower(type) LIKE lower(type)'
        self.__cursor.execute(query, (f'%{type}%',))
        rows = self.__cursor.fetchall()
        return self.__getCprSets(rows)

    def deleteAllCprFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos los cpr que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM CPR WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
