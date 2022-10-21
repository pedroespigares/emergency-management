import os
import sys
sys.path.append(os.path.abspath('..'))

import sqlite3
from Clases.medication import Medication
from Clases.urgency import Urgency


class MedicationManager:
    '''
    Gestiona los objetos de la clase Medication en la base de datos
    '''

    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getMedicationSets(self, rows):
        '''
        Crea un objeto Medication a partir registros de la base de datos

        rows = lista registro de la base de datos
        resultado = Medicaciones(Medication)
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
            obtainedMedication = Medication(
                self.__connection,
                obtainedUrgency,
                row["name"],
                row["dosage"],
            )
            result.add(obtainedMedication)
        return result

    def getMedicationBaseSQL(self):
        '''
        Contiene las consultas de los métodos de colecciones
        de medicaciones
        resultado = devuelve el contenido de las consultas
        '''

        query = 'SELECT urgency, name, dosage '
        query += 'FROM Medication '
        return query

    def getAllMedication(self):
        '''
        Devuelve una coleccion con todos los objetos tipo Medication
        de la base de datos.

        resultado = devolvera un conjunto de objetos tipo Medication
        '''

        query = 'SELECT urgency, name, dosage '
        query += 'FROM Medication'
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getMedicationSets(rows)

    def getMedicationByUrgencies(self, *urgency):
        '''
        Devuelve una coleccion de objetos tipo Medication según
        sus urgencias.

        urgency = coleccion de urgencias correspondientes a Medication
        resultado = devolvera un conjunto de objetos tipo Medication
        '''

        query = self.getMedicationBaseSQL()
        if len(urgency) > 1:
            query += 'WHERE urgency IN {}'.format(urgency)
        elif len(urgency) == 1:
            query += 'WHERE urgency = {}'.format(urgency[0])
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return self.__getMedicationSets(rows)

    def getMedicationByUrgency(self, urgency):
        '''
        Devuelve una coleccion de objetos tipo Medication según
        parte del episodio de la urgencia

        urgency = contendrá parte del episodio de la urgencia
        de una medicación (str)
        resultado = devolvera un conjunto de objetos tipo Medication
        '''

        query = self.getMedicationBaseSQL()
        query += 'WHERE urgency LIKE ?'
        self.__cursor.execute(query, (f'%{urgency}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicationSets(rows)

    def getMedicationByName(self, name):
        '''
        Devuelve una coleccion de objetos tipo Medication segun su nombre

        name = contendrá parte del nombre de una Medication (str)
        resultado = devolvera un conjunto de objetos tipo Medication
        '''

        query = self.getMedicationBaseSQL()
        query += 'WHERE lower(name) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{name}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicationSets(rows)

    def getMedicationByDosage(self, dosage):
        '''
        Devuelve una coleccion de objetos tipo Medication segun su dosis

        dosage = contendrá parte de la dosis de una Medication (str)
        resultado = devolvera un conjunto de objetos tipo Medication
        '''

        query = self.getMedicationBaseSQL()
        query += 'WHERE lower(dosage) LIKE lower(?)'
        self.__cursor.execute(query, (f'%{dosage}%',))
        rows = self.__cursor.fetchall()
        return self.__getMedicationSets(rows)

    def deleteAllMedicationFromUrgency(self, urgencyToDelete):
        '''
        Borra de la base de datos todos las medicaciones que tengan como
        urgencia el pasado por parámetro
        '''

        query = 'DELETE FROM Medication WHERE urgency = ?'
        self.__cursor.execute(query, (urgencyToDelete.getEpisode(),))
        self.__connection.commit()
