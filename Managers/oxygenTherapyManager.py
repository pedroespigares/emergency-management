import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.oxygenTherapy import OxygenTherapy
from Clases.urgency import Urgency


class OxygenTherapyManager:
    '''
    Gestiona los objetos de la clase OxygenTherapy en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getOxygenTherapySets(self, rows):
        '''
        Crea un objeto OxygenTherapy a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Análisis(OxygenTherapy)
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
            obtainedOxygenTherapy = OxygenTherapy(
                self.__connection,
                obtainedUrgency,
                row["therapy"],
            )
            result.add(obtainedOxygenTherapy)
        return result

    def getOxygenTherapyBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de RCP
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, therapy '
        query += 'FROM Oxygen_therapy '
        return query

    def getAllOxygenTherapy(self):
        '''
        Devuelve una coleccion con todos los objetos tipo OxygenTherapy
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo OxygenTherapy
        '''

        query = 'SELECT urgency, therapy '
        query += 'FROM Oxygen_therapy'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getOxygenTherapySets(rows)

    def getOxygenTherapyByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo OxygenTherapy según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a OxygenTherapy
        resultado = devolvera un conjunto de objetos tipo OxygenTherapy
        '''

        query = self.getOxygenTherapyBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getOxygenTherapySets(rows)

    def getOxygenTherapyByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo OxygenTherapy según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la urgencia de
        una oxigenoterapia (str)
        resultado = devolvera un conjunto de objetos tipo OxygenTherapy
        '''

        query = self.getOxygenTherapyBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getOxygenTherapySets(rows)

    def getOxygenTherapyByTherapy(self, therapy):
        '''
        Devuelve una coleccion de objetos tipo OxygenTherapy segun su terapia

        therapy = contendrá parte de la terapia de una oxigeno terapia (str)
        resultado = devolvera un conjunto de objetos tipo OxygenTherapy
        '''

        query = self.getOxygenTherapyBaseSQL()
        query += 'WHERE lower(therapy) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{therapy}%',))
        rows = self.__cursor.fetchall()
        return self.__getOxygenTherapySets(rows)

    def deleteAllOxygenTherapyFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos las oxigenoterapias que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Oxygen_Therapy WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
