import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.treatment import Treatment
from Clases.urgency import Urgency


class TreatmentManager:
    '''
    Gestiona los objetos de la clase Treatment en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getTreatmentSets(self, rows):
        '''
        Crea un objeto Treatment a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Tratamiento(Treatment)
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
            obtainedTreatment = Treatment(
                self.__connection,
                obtainedUrgency,
                row["type"],
                row["antitetanus"],
                row["anesthesia"],
            )
            result.add(obtainedTreatment)
        return result

    def getTreatmentBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de análisis
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, type, antitetanus, anesthesia '
        query += 'FROM Treatment '
        return query

    def getAllTreatment(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Treatment
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Treatment
        '''

        query = 'SELECT urgency, type, antitetanus, anesthesia '
        query += 'FROM Treatment'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getTreatmentSets(rows)

    def getTreatmentByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Treatment según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a Treatment
        resultado = devolvera un conjunto de objetos tipo Treatment
        '''

        query = self.getTreatmentBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getTreatmentSets(rows)

    def getTreatmentByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Treatment según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la urgencia
        de un tratamiento (str)
        resultado = devolvera un conjunto de objetos tipo Treatment
        '''

        query = self.getTreatmentBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getTreatmentSets(rows)

    def getTreatmentByType(self, type):
        '''
        Devuelve una coleccion de objetos tipo Treatment segun su tipo

        petition = contendrá parte del tipo de un tratamiento (str)
        resultado = devolvera un conjunto de objetos tipo Treatment
        '''

        query = self.getTreatmentBaseSQL()
        query += 'WHERE lower(type) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{type}%',))
        rows = self.__cursor.fetchall()
        return self.__getTreatmentSets(rows)

    def getTreatmentByAntitetanus(self, antitetanus):
        '''
        Devuelve una coleccion de objetos tipo Treatment segun si el paciente
        tiene la vacuna contra el tétanos o no.

        antitetanus = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Treatment
        '''

        query = self.getTreatmentBaseSQL()
        query += 'WHERE antitetanus = ?'
        antitetanus = antitetanus.strip()
        self.__cursor.execute(query, (antitetanus,))
        rows = self.__cursor.fetchall()
        return self.__getTreatmentSets(rows)

    def getTreatmentByAnesthesia(self, anesthesia):
        '''
        Devuelve una coleccion de objetos tipo Treatment segun si el paciente
        ha necesitado anestesia o no.

        anesthesia = (str)
        - 0 --> No
        - 1 --> Sí
        resultado = devolvera un conjunto de objetos tipo Treatment
        '''

        query = self.getTreatmentBaseSQL()
        query += 'WHERE anesthesia = ?'
        anesthesia = anesthesia.strip()
        self.__cursor.execute(query, (anesthesia,))
        rows = self.__cursor.fetchall()
        return self.__getTreatmentSets(rows)

    def deleteAllTreatmentFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos los tratamientos que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Treatment WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
